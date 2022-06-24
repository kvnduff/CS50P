"""
CS50 P-shirt creator
"""

import sys
from PIL import Image, ImageOps


def main():

    # Command line argument number check
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Input/output file extension check
    _, input_ext = sys.argv[1].split(".")
    _, output_ext = sys.argv[2].split(".")
    ext = ["jpg", "jpeg", "png"]
    if input_ext not in ext:
        sys.exit("Invalid input")
    if output_ext not in ext:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Get size of shirt.png
    shirt = Image.open("shirt.png")
    size = shirt.size

    # Open input file
    try:
        raw_img = Image.open(sys.argv[1])

        # Resize/crop input file to size of shirt.png
        upd_img = ImageOps.fit(raw_img, size)

        # Overlay shirt on resized/cropped input file
        upd_img.paste(shirt, shirt)

        # Save resulting image
        upd_img.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
