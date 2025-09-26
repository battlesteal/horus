from rich import print

WEATHER_ICONS: dict[str, tuple[str, ...]] = {
    "clear": (
        "[yellow]   \\   /   [/yellow]",
        "[yellow]    .-.    [/yellow]",
        "[yellow] — (   ) — [/yellow]",
        "[yellow]    `-'    [/yellow]",
        "[yellow]   /   \\   [/yellow]",
    ),
    "partly_cloudy": (
        "[yellow]   \\  /    [/yellow]",
        "[yellow] _ /\"\"[/yellow][white].-.  [/white]",
        "[yellow]   \\_[/yellow][white](   ).[/white]",
        "[yellow]   /[/yellow][white](___(__)[/white]",
        "             ",
    ),
    "cloudy": (
        "             ",
        "[white]    .--.   [/white]",
        "[white] .-(    ). [/white]",
        "[white](___.__)__)[/white]",
        "           ",
    ),
    "light rain": (
        "[white]    .-.    [/white]",
        "[white]   (   ).   [/white]",
        "[white]  (___(__) [/white]",
        "[blue]   ' ' ' ' [/blue]",
        "[blue]  ' ' ' '  [/blue]",
    ),
    "moderate rain": (
        "[white]    .-.    [/white]",
        "[white]   (   ).   [/white]",
        "[white]  (___(__) [/white]",
        "[blue]  ‚‘‚‘‚‘‚‘  [/blue]",
        "[blue]  ‚’‚’‚’‚’  [/blue]",
    ),
    "heavy rain": (
        "[white]    .-.    [/white]",
        "[white]   (   ).   [/white]",
        "[white]  (___(__) [/white]",
        "[blue]  //////// [/blue]",
        "[blue]  ///////  [/blue]",
    ),
    "thunderstorm": (
           "[white]     .--.  [/white]",
           "[white] .-(    ). [/white]",
           "[white](___.__)__)[/white]",
           "[blue]'[/blue][yellow]⚡[/yellow][blue]',[/blue][yellow]⚡[/yellow][blue]'[/blue][yellow]⚡[/yellow][blue]',  [/blue]",
           "[blue]',',',',','[/blue]",
    ),
    "fog": (
        "[white] _ - _ - _ - [/white]",
        "[white]  _ - _ - _  [/white]",
        "[white] _ - _ - _ - [/white]",
        "[white]  _ - _ - _  [/white]",
        "[white] _ - _ - _ - [/white]",
    ),
    "light snow": (
        "[white]    .-.    [/white]",
        "[white]   (   ).   [/white]",
        "[white]  (___(__) [/white]",
        "[cyan]   *  *  * [/cyan]",
        "[cyan]  *  *  *  [/cyan]",
    ),
    "moderate snow": (
        "[white]    .-.    [/white]",
        "[white]   (   ).   [/white]",
        "[white]  (___(__) [/white]",
        "[cyan]  * * * *  [/cyan]",
        "[cyan] * * * *   [/cyan]",
    ),
    "heavy snow": (
    "[white]    .--.   [/white]",
    "[white] .-(    ). [/white]",
    "[white](___.__)__)[/white]",
    "[cyan] * * * * * [/cyan]",
    "[cyan]* * * * * *[/cyan]",
    ),
}


for icon_name, icon_lines in WEATHER_ICONS.items():
    print(f"{icon_name}:")
    for line in icon_lines:
        print(f"{line:<11}")
    print()