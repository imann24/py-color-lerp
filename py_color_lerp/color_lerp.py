from colour import Color

class ColorLerp:
    def __init__(self, start_color:Color, end_color:Color):
        self.start_color = start_color
        self.end_color = end_color

    def lerp(self, progress:float) -> Color:
        red = ColorLerp.linear_interpolate(self.start_color.red, self.end_color.red, progress)
        green = ColorLerp.linear_interpolate(self.start_color.green, self.end_color.green, progress)
        blue = ColorLerp.linear_interpolate(self.start_color.blue, self.end_color.blue, progress)
        return Color(red=red, green=green, blue=blue)
    
    def lerp_to_hex_color(self, progress:float) -> str:
        return self.lerp(progress).hex

    @classmethod
    def linear_interpolate(cls, start:float, end:float, progress:float) -> float:
        return (progress * start) + ((1 - progress) * end)
        
