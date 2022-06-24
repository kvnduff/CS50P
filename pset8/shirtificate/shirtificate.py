"""
Generate pdf document with image of a shirt overlayed with a message
"""

from fpdf import FPDF


def main():

    # Instantiate pdf object
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add image
    add_image(pdf)

    # Add document title
    add_title(pdf)

    # Get user name
    name = input("Name: ")

    # Add name to shirt
    add_name(pdf, name)

    # Generate pdf file
    pdf.output("shirtificate.pdf")


def add_image(pdf):
    """
    Add image to pdf
    """
    pdf.image("shirtificate.png", 10, 70, 190)


def add_title(pdf):
    """
    Add title to pdf
    """
    pdf.set_font("helvetica", "", 50)
    pdf.cell(190, 40, "CS50 Shirtificate", align="C")


def add_name(pdf, name):
    """
    Add name to shirt message.
    """
    pdf.set_font("helvetica", "", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-190, 250, f'{name} took CS50', align='C')


if __name__ == "__main__":
    main()
