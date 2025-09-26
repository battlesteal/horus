from pathlib import Path

ROOT_DIR = Path(__file__).parent

# Default settings
# If no location is provided via command line arguments, these defaults will be used
# If you want to set a default location, change the values below
# For example:
# DEFAULT_CITY = "New York"
# DEFAULT_STATE = "NY"
# DEFAULT_COUNTRY = "US"
# DEFAULT_LATITUDE = 40.7306
# DEFAULT_LONGITUDE = -73.9352
# If you do not want to set a default location, leave them as None
DEFAULT_CITY = None
DEFAULT_STATE = None
DEFAULT_COUNTRY = None
DEFAULT_LATITUDE = None
DEFAULT_LONGITUDE = None

# Default unit group for temperature and other measurements
# Options are "us", "metric", and "base"
# "us" = Fahrenheit, inches
# "metric" = Celsius, millimeters
# "base" = Kelvin, millimeters
DEFAULT_UNIT_GROUP = "us" 