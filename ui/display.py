from rich import print, box
from rich.panel import Panel
from rich.columns import Columns

from weather import Weather, WeatherReport 

def _determine_buffer_space(value: float) -> str:
    if value < 10:
        return "  "
    elif value < 100:
        return " "
    else:
        return ""

def weather_day_panel(weather: Weather, title: str) -> Panel:
    """Create and display a panel for a single day's weather."""
    panel_title = f"[bold]{title}[/bold]"

    condition_desc = weather.conditions.desc_short[:11].center(11)
    condition_icon = weather.conditions.icon

    hum_buffer_space = _determine_buffer_space(weather.humidity)
    precip_perc_buffer_space = _determine_buffer_space(weather.precip_probability)


    body_lines = [
        f"{condition_icon[0]} Temperature: [bold]{weather.temperature:3.1f}°F[/bold]",
        f"{condition_icon[1]} Feels Like:  [bold]{weather.feels_like:3.1f}°F[/bold]",
        f"{condition_icon[2]} Humidity:    [bold]{weather.humidity:3.1f}{hum_buffer_space}%[/bold]",
        f"{condition_icon[3]} Dew Point:   [bold]{weather.dew:3.1f}°F[/bold]",
        f"{condition_icon[4]} Precip:      [bold]{weather.precip:3.1f} in[/bold]",
        f"{condition_desc} Precip %:    [bold]{weather.precip_probability:3.1f}{precip_perc_buffer_space}%[/bold]"
    ]

    # condition_desc_padded = _condition_desc_with_padding(weather.conditions.description, 12)
    # precip_amount = f"Precip Amount: [bold]{weather.precip} in[/bold]"
    # body_lines.append(condition_desc_padded + precip_amount)

    body = "\n".join(body_lines)


    panel = Panel.fit(body, title=panel_title, box=box.SQUARE)
    return panel

def display_weather_report(report: WeatherReport) -> None:
    """Display the weather report in the terminal."""
    current_panel = weather_day_panel(report.current, "Current")

    forecast_panels = []
    for day in report.forecast:
        panel = weather_day_panel(day, day.datetime)
        forecast_panels.append(panel)

    print(current_panel)
    print(Columns(forecast_panels, expand=False, equal=True))