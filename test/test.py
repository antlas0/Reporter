#!/usr/bin/env python3


"""
copyright (c), 2021 antlas
"""


def test_generate_pdf():
    """[summary]
    Generate a pdf report
    """
    from src.serialisers.pdf import PDFSerialiser
    from src.resources import PDFDetails

    generator = PDFSerialiser()
    details = PDFDetails(
        author1="Antoine L.",
        email1="",
        title1="Important title",
        image1="./test/data/images/lin.jpg"
    )
    generator.set_working_dir("output")
    res = generator.serialise("test.pdf", details)
    assert(res)
