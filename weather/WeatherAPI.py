import os
import sys
import time
from datetime import datetime

import httpx
from dotenv import load_dotenv

from config import ROOT_DIR 
from .types import Location, Weather, WeatherReport
from . import cache

load_dotenv()

cache_file = ROOT_DIR / "weather_cache.json"

class WeatherAPI:
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    api_key: str | None = os.getenv("APIKEY")

    def __init__(self, location: Location, params: dict | None = None) -> None:
        self.location = location
        self.params = params or {}
        self.params["key"] = self.api_key
        self.params["unitGroup"] = self.params.get("unitGroup", "us")
        self.params["contentType"] = self.params.get("contentType", "json")
        self.params["include"] = self.params.get("include", ["current"])
        self.params["lang"] = self.params.get("lang", "id")

    def _location_str(self) -> str:
        if self.location.city and self.location.country:
            if self.location.state:
                return f"{self.location.city},{self.location.state},{self.location.country}"
            else:
                return f"{self.location.city},{self.location.country}"
        elif self.location.latitude and self.location.longitude:
            return f"{self.location.latitude},{self.location.longitude}"
        else:
            raise ValueError("Invalid location data")

    def _parse_weather_data(self, data: dict) -> WeatherReport:
        current_data = Weather.from_dict(data.get("currentConditions", {}), "current")
        forecast_data = [Weather.from_dict(day, "forecast") for day in data.get("days", [])[:7]]
        return WeatherReport(location=self.location, current=current_data, forecast=forecast_data)

    def get_weather(self) -> WeatherReport:
        """Fetch current weather data and a forecast for the next 7 days."""
        current_time = datetime.now()
        cached_weather_data: list[dict] = cache.load_weather_cache()
        if cached_weather_data:
            existing_cache: dict = cache.check_for_existing_cached_data(
                location=self.location,
                cached_data=cached_weather_data,
                current_time=current_time
            )
            if existing_cache:
                return self._parse_weather_data(existing_cache)
            cache.remove_expired_cache_data(cached_data=cached_weather_data, current_time=current_time)

        url = f"{self.BASE_URL}{self._location_str()}"
        response = httpx.get(url, params=self.params)

        if response.status_code == 421:
            for _ in range(3):
                time.sleep(5)
                response = httpx.get(url, params=self.params)
            
                if response.status_code == 200:
                    break
            response.raise_for_status()
        elif response.status_code == 401:
            print(f"Invalid API key. Please check that your API key is in {ROOT_DIR}/.env, is valid, and try again.")
            print("You can obtain a free API key by creating an account at https://www.visualcrossing.com/weather-api")
            sys.exit()
        response.raise_for_status()

        response_data: dict = response.json()
        cache.cache_weather(data=response_data, location=self.location, current_time=current_time)
        return self._parse_weather_data(response_data)

    # def get_hourly_forecast(self) -> list[dict]:
    #     if "hours" not in self.params["include"]:
    #         self.params["include"].append("hours")
    #     weather_data = self.get_weather()
    #     return weather_data.get("days", [])[0].get("hours", [])
