from colour import Color

from py_color_lerp import ColorLerp

def test_lerp():
    color = ColorLerp(Color("red"), Color("blue"))
    
    purple = color.lerp(0.5)

    assert round(purple.red, 1) == round(Color("purple").red, 1)
    assert round(purple.green, 1) == round(Color("purple").green, 1)
    assert round(purple.blue, 1) == round(Color("purple").blue, 1)

def test_lerp_hex():
    color = ColorLerp(Color("red"), Color("blue"))
    
    purple_hex = color.lerp_to_hex_color(0.5)

    assert purple_hex == "#7f007f"
