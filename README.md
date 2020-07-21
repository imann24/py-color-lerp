# Python Color Lerp
Interpolate between two colors in Python

## Example Usage
```python
from colour import Color

from py_color_lerp import ColorLerp

color = ColorLerp(Color("red"), Color("blue"))
    
# returns hexadecimal color purple as string: "#7f007f"
purple_hex = color.lerp_to_hex_color(0.5)
```

## Dev Commands 
1. `poetry install` :: install dependencies
1. `poetry run pytest` :: execute unit tests
