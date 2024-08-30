from utils.pre_process import _extract_name


def test_extract_name():
    filenmae = "F4E-OMF-1159-01-01-36 Monthly Report Marc Ferrater #19 M07 2024.docx"
    name = _extract_name(filenmae)
    assert name == "Marc Ferrater"
