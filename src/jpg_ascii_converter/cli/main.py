import click
from copy import copy

from jpg_ascii_converter.service import JPGASCIIConverter
from jpg_ascii_converter.constants import MAX_RGB_VALUE, SCALE_FACTOR, SINGLE_CHAR_HEIGHT, SINGLE_CHAR_WIDTH


@click.command()
@click.argument("image_path")
@click.option("-m", "--max_rgb_value", required=False, help=f"Max RGB value, default {MAX_RGB_VALUE}.")
@click.option("-s", "--scale_factor", required=False, help=f"Scale factor, default {SCALE_FACTOR}.")
@click.option("-h", "--single_char_height", required=False, help=f"Single char height, default {SINGLE_CHAR_HEIGHT}.")
@click.option("-w", "--single_char_width", required=False, help=f"Single char width, default {SINGLE_CHAR_WIDTH}.")
def main(
        image_path: str = None, 
        max_rgb_value: float = None,
        scale_factor: float = None,
        single_char_height: float = None,
        single_char_width: float = None
    ):
    args = copy(locals())
    params = {}
    for arg, val in args.items():
        if arg == "image_path":
            continue
        if val:
            params[arg] = float(val)
    converter = JPGASCIIConverter(
        **params
    )
    converter.convert(image_path=image_path)
