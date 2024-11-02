import math
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


from ..constants import CHARS, MAX_RGB_VALUE, SINGLE_CHAR_HEIGHT, SINGLE_CHAR_WIDTH, SCALE_FACTOR


class JPGASCIIConverter:
    def __init__(self,
        chars: str = CHARS,
        font: str = None,
        max_rgb_value: float = MAX_RGB_VALUE,
        scale_factor: float = SCALE_FACTOR,
        single_char_height: float = SINGLE_CHAR_HEIGHT,
        single_char_width: float = SINGLE_CHAR_WIDTH,
    ):
        self._chars = list(chars)
        self._font = ImageFont.truetype(font) if font else None
        self._max_rgb_value = max_rgb_value
        self._scale_factor = scale_factor
        self._single_char_height = single_char_height
        self._single_char_width = single_char_width

    @property
    def density_interval(self):
        return len(self._chars) / self._max_rgb_value
    
    @property
    def character_scale(self):
        return self._single_char_width / self._single_char_height

    def _get_char(self, char_input: int):
        return self._chars[math.floor(char_input * self.density_interval)]
    
    def _get_image_name_and_suffix(self, image_path):
        path = Path(image_path)
        return path.name, path.suffix
    
    def _scale_image(self, image: Image):
        original_width, original_height = image.size
        return image.resize(
            (int(self._scale_factor * original_width),
            int(self._scale_factor * original_height * self.character_scale)),
            Image.NEAREST
        )

    def convert(self, image_path: str = None):
        if image_path:
            if os.path.exists(image_path):
                image = Image.open(image_path)
                scaled_image = self._scale_image(image)
                scaled_width, scaled_height = scaled_image.size
                buffer = scaled_image.load()
                canvas = Image.new(
                    "RGB", 
                    (self._single_char_width * scaled_width, self._single_char_height * scaled_height),
                    color = (0,0,0)
                )
                ascii_draw = ImageDraw.Draw(canvas)

                for i in range(scaled_height):
                    for j in range(scaled_width):
                        r, g, b = buffer[j, i]
                        value = int((r + g + b) / 3)
                        buffer[j, i] = (value, value, value)

                        ascii_draw.text(
                            (
                                j * self._single_char_width,
                                i * self._single_char_height
                            ),
                            self._get_char(value),
                            font = self._font,
                            fill = (r, g, b)
                        )

                name, suffix = self._get_image_name_and_suffix(image_path)
                canvas.save(f"ascii_{name.replace(suffix, '')}.png")
                return
            raise FileNotFoundError()
        raise Exception("Image path cannot be empty.")
