from utils.process_dms import parse_DMS


def test_parse_DMS():
    df = parse_DMS()
    assert df.loc["Eduard Carbonell", "2025", "January"]["DMS"] == "ATG-EU-RP-PC-F4E-24-07463"
    assert (
        df.loc["Marc Ferrater", "2024", "August"]["DMS"] == "ATG-NL-RP-PC-F4E-23-00125"
    )
