from rich.console import Console

from rich.theme import Theme

from rich.table import Table

from rich.panel import Panel


custom_theme = Theme({"success": "green", "error":"bold red"})
console = Console(theme = custom_theme)

console.print("Operation Successful", style = "success")
console.print("Operation Failed", style ="error")


table = Table(title="Weather")

table.add_column("Date", justify="center", style="success", no_wrap=True)
table.add_column("Temperature", style="error")
table.add_column("Forecast", justify="center", style="blue")

table.add_row("Dec 20, 2019", "66F", "Sunny with light rain")


console.print(Panel(table))


