import argparse
from rich import print

import config
import weather
import ui.display as display
from weather import WeatherAPI, cache


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "-c",
        "--city",
        type=str,
        help="City name",
        default=config.DEFAULT_CITY
    )
    parser.add_argument(
        "-s",
        "--state",
        type=str,
        help="State code (if applicable)",
        default=config.DEFAULT_STATE
    )
    parser.add_argument(
        "-C",
        "--country",
        type=str,
        help="Country code",
        default=config.DEFAULT_COUNTRY
    )
    parser.add_argument(
        "-lat",
        "--latitude",
        type=float,
        help="Latitude coordinate",
        default=config.DEFAULT_LATITUDE
    )
    parser.add_argument(
        "-lon",
        "--longitude",
        type=float,
        help="Longitude coordinate",
        default=config.DEFAULT_LONGITUDE
    )
    parser.add_argument(
        "-u",
        "--unit-group",
        type=str,
        choices=["us", "metric", "base"],
        help="Unit group for temperature and other measurements (us, metric, base)",
        default=config.DEFAULT_UNIT_GROUP
    )
    parser.add_argument(
        "-x",
        "--clear-cache",
        action="store_true",
        help="Clear the weather cache",
        dest="clear_cache"
    )

    args = parser.parse_args()
    if args.clear_cache:
        return args

    if not ((args.city and args.country) or (args.latitude and args.longitude)):
        parser.error("You must provide either city and country, or latitude and longitude.")

    if (args.city or args.country) and (args.latitude or args.longitude):
        parser.error("Provide either city/country or latitude/longitude, not both.")

    return args

def print_weather(weather: weather.Weather) -> None:
    print(f"Date/Time: {weather.datetime}")
    print(f"Conditions: {weather.conditions.description}")
    for line in weather.conditions.icon:
        print(line)
    print(f"Temperature: {weather.temperature}°")
    print(f"Feels Like: {weather.feels_like}°")
    print(f"Humidity: {weather.humidity}%")
    print(f"Dew Point: {weather.dew}°")
    print(f"Precipitation Probability: {weather.precip_probability}%")
    print(f"Precipitation Amount: {weather.precip} inches")

def main() -> None:
    args = get_args()
    if args.clear_cache:
        cache.clear_weather_cache()
        return

    location = weather.Location(
        city=args.city,
        state=args.state,
        country=args.country,
        latitude=args.latitude,
        longitude=args.longitude
    )

    api_client = WeatherAPI(location)
    weather_data: weather.WeatherReport = api_client.get_weather()

    display.display_weather_report(weather_data)
    


if __name__ == "__main__":
    main()