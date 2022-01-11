from rich import print
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
    
)
layout["upper"].size = 10
layout["upper"].visible = False
print(layout)

layout.split_row(
    Layout(name="left"),
    Layout(name="right")   
)

print(layout)

layout["right"].split(
    Layout(Panel("Hello")),
    Layout(Panel("World!"))
)

layout["left"].update(
    "The mystery of life isn't a problem to solve, but a reality to experience."
)
print(layout)

print(layout.tree)