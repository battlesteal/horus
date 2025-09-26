from typing import Optional
from dataclasses import dataclass

from . import conditions as cond

@dataclass
class Location:
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self):
        city_country_provided = self.city is not None and self.country is not None
        lat_lon_provided = self.latitude is not None and self.longitude is not None
        if city_country_provided and lat_lon_provided:
            raise ValueError("Provide either city/country or latitude/longitude, not both.")
        if not city_country_provided and not lat_lon_provided:
            raise ValueError("You must provide either city/country or latitude/longitude.")
    
    def dict(self) -> dict:
        return {
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

@dataclass
class Weather:
    datetime: str
    conditions: cond.Condition
    temperature: float
    feels_like: float
    humidity: int
    dew: float
    precip_probability: float
    precip: float

    @staticmethod
    def _get_condition(api_conditions: str) -> cond.Condition:
        provided_conditions = api_conditions.split(", ")
        return cond.CONDITIONS.get(provided_conditions[0], cond.Condition(description="Unknown", icon=cond.ICONS["unknown"]))

    @classmethod
    def from_dict(cls, data: dict, weather_type: str) -> "Weather":
        condition = cls._get_condition(data.get("conditions", "Unknown"))
        return cls(
            datetime=data.get("datetime", ""),
            conditions=condition,
            temperature=data.get("temp", 0.0) if weather_type == "current" else data.get("tempmax", 0.0),
            feels_like=data.get("feelslike", 0.0),
            humidity=data.get("humidity", 0),
            dew=data.get("dew", 0.0),
            precip_probability=data.get("precipprob", 0.0),
            precip=data.get("precip", 0.0),
        )

@dataclass
class WeatherReport:
    location: Location
    current: Weather
    forecast: list[Weather]  # 7 items for 7 days
    