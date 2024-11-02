# ASCII Artwork Converter

The ASCII Artwork Converter is a simple tool that converts `.jpg` images into ASCII art. It provides flexibility in the ASCII conversion process, allowing you to adjust multiple parameters like scale, font, and characters used for the conversion.

## Getting Started

To get started with the ASCII Artwork Converter, ensure you have a `.jpg` image file and specify its path when using the CLI command `jpg_ascii`. Additionally, if you're on Windows or macOS, adjust the `font` variable path, as this project was developed on Linux.

### Installation

Clone this repository and navigate into the project directory:

```bash
git clone <repository_url>
cd ASCII-Art-Converter
```

```bash
pip install .
```

## CLI Command: jpg_ascii
The jpg_ascii command converts a specified .jpg image to ASCII art. You can customize the ASCII art's resolution, scale, and character dimensions.

### Usage
```bash
jpg_ascii <image_path> -s <scale_factor> -h <single_char_height> -w <single_char_width>
```
- image_path: Path to the .jpg image file to be converted.
- scale_factor: Scaling factor for the ASCII art resolution. Suggested values are between 0.2 and 0.8.
- single_char_height: Height of each character in the ASCII art.
- single_char_width: Width of each character in the ASCII art.

#### Customizable Variables
You can adjust the following variables in the code to control the ASCII conversion:

- SINGLE_CHAR_HEIGHT: Defines the height of each character in the ASCII output.
- SINGLE_CHAR_WIDTH: Defines the width of each character in the ASCII output.
- SCALE_FACTOR: Controls how scaled the output ASCII art is relative to the original image resolution.
- font: Specifies the font used for ASCII characters, with the path to the font file.
- chars: A list of characters used to render the ASCII image, from densest to least dense.

## Important Notes
Ensure the image file is a .jpg format and set its path in the image_path argument.

Happy ASCII art creation!
