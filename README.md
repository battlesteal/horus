This is a fairly simple weather TUI. It was written more as practice than anything else. This README (after this point) was written using AI because I had no desire to actually write one myself. I expect exactly 0 other people to ever see this repository better yet download and run the project.

# Horus Weather Terminal App

Horus is a terminal-based weather application that fetches and displays current conditions and a 7-day forecast using the Visual Crossing Weather API. It features a text-based user interface (TUI) with ASCII art icons and supports caching for efficient API usage.

## Features
- Fetches current weather and 7-day forecast for a specified location
- Terminal UI with ASCII art and colored output (using `rich`)
- Caching to minimize API calls
- Configurable via command-line arguments and `.env` file

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/battlesteal/horus.git
cd horus
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Set Up Your API Key
Create a `.env` file in the project root with your Visual Crossing API key:
```
APIKEY=your_api_key_here
```
You can obtain a free API key at https://www.visualcrossing.com/weather-api

### 5. Run the Application
```bash
python horus.py -c <city> -s <state> -C <country>
or
python horus.py -lat <latitude> -lon <longitude>
```
Example:
```bash
python horus.py -c "New York" -s NY -C US
python horus.py -lat 40.7306 -lon -73.9353
```

## Command-Line Arguments
- `-c`, `--city`: City name
- `-s`, `--state`: State or region (optional)
- `-C`, `--country`: Country code
- `-lat`, `--latitude`: Latitude (alternative to city/country)
- `-lon`, `--longitude`: Longitude (alternative to city/country)
- `-x`, `--clear-cache`: Clear the weather cache.

## Project Structure
```
├── horus.py            # Main entry point
├── config.py           # Configuration and root directory
├── requirements.txt    # Python dependencies
├── .env                # API key (not tracked by git)
├── weather/            # Weather logic, API, caching, types, conditions
|   ├── __init__.py
│   ├── WeatherAPI.py
│   ├── cache.py
│   ├── types.py
│   └── conditions.py
├── ui/
|   └── display.py
└── ...
```

