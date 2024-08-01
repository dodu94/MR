from utils.process_dms import parse_DMS


def test_parse_DMS():
    df = parse_DMS()
    assert (
        df.loc["Davide Laghi", "2024", "July"]["DMS"].values[0]
        == "ATG-NL-RP-PC-F4E-23-00262"
    )
