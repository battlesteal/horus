import json
from datetime import datetime

from config import ROOT_DIR
from .types import Location

cache_file = ROOT_DIR / "weather_cache.json"

def clear_weather_cache() -> None:
    """Clear the weather cache by deleting the cache file."""
    if cache_file.exists():
        cache_file.unlink()
        print("Cache cleared.")
        return
    print("No cache file to clear.")

def load_weather_cache() -> list[dict]:
    """Load the weather cache from the JSON file."""
    if not cache_file.exists():
        return []

    with open(cache_file, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            return []

def _matching_location(loc1: Location, loc2: dict) -> bool:
    """Check if two locations match."""
    if loc1.city and loc1.country:
        return (
            loc1.city == loc2.get("city") and
            loc1.state == loc2.get("state") and
            loc1.country == loc2.get("country")
        )
    elif loc1.latitude and loc1.longitude:
        return (
            loc1.latitude == loc2.get("latitude") and
            loc1.longitude == loc2.get("longitude")
        )
    return False

def check_for_existing_cached_data(
    location: Location, cached_data: list[dict], current_time: datetime
) -> dict:
    """Check for existing cached data for the given location. Return it if found and not expired."""
    for entry in cached_data:
        if "location" in entry:
            loc: dict = entry["location"]
            if _matching_location(location, loc):
                if "cached_at" not in entry:
                    continue
                cached_time = datetime.fromisoformat(entry["cached_at"])
                time_diff = (current_time - cached_time).total_seconds() / 60
                if time_diff <= 30:
                    return entry
            else:
                continue
        else:
            continue

    return {}


def cache_weather(data: dict, location: Location, current_time: datetime) -> None:
    if not cache_file.exists():
        cache_file.touch()

    cached_data: list[dict] = load_weather_cache()

    data["cached_at"] = current_time.isoformat()
    data["location"] = location.dict()
    cached_data.append(data)

    with open(cache_file, "w") as file:
        json.dump(cached_data, file, indent=4)


last_cache_cleanup: datetime | None = None
def remove_expired_cache_data(cached_data: list[dict], current_time: datetime) -> None:
    """Remove expired cache entries older than 30 minutes."""
    # Check if the last cache cleanup was within the last 30 minutes
    # If the last cleanup was more than 30 minutes ago or is None, proceed with cleanup
    global last_cache_cleanup
    if last_cache_cleanup:
        time_diff = (current_time - last_cache_cleanup).total_seconds() / 60
        if time_diff <= 30:
            return

    valid_entries = []
    for entry in cached_data:
        if "cached_at" in entry:
            cached_time = datetime.fromisoformat(entry["cached_at"])
            time_diff = (current_time - cached_time).total_seconds() / 60
            if time_diff <= 30:
                valid_entries.append(entry)

    with open(cache_file, "w") as file:
        json.dump(valid_entries, file, indent=4)

    last_cache_cleanup = current_time