import os
import pytest

from jpg_ascii_converter.service import JPGASCIIConverter


def test_jpg_ascii_converter_raises_if_no_image_path_is_supplied():
    with pytest.raises(Exception):
        converter = JPGASCIIConverter()

        converter.convert()

def test_jpg_ascii_converter_raises_file_not_found_error_if_image_is_not_found():
    with pytest.raises(FileNotFoundError):
        converter = JPGASCIIConverter()

        converter.convert("./tests/test_not_exist.jpg")

def test_jpg_ascii_converter_converts():
    converter = JPGASCIIConverter()

    converter.convert("./tests/test_image.jpg")
    assert os.path.exists("./ascii_test_image.png")
    os.remove("./ascii_test_image.png")

    assert not os.path.exists("./ascii_test_image.png")
