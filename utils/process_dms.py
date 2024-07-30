import pandas as pd
import re


def parse_DMS() -> pd.DataFrame:
    pat_year = re.compile(r"\d+")
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    dummy_tag = "Monthly Report"
    dms = pd.read_csv("DMS_numbers.csv")
    rows = []
    for value in dms["Description"].values:
        try:
            year = pat_year.search(value).group()
        except AttributeError:
            print(f"{value} could not be parsed")
            continue

        for month in months:
            if month in value:
                break
        for string in [dummy_tag, month, year]:
            value = value.replace(string, "")
        name = value.strip()
        rows.append(
            {
                "Name": name,
                "Month": month,
                "Year": year,
            }
        )
    dms_new = pd.DataFrame(rows)
    dms_new["DMS"] = dms["Reference"]
    return dms_new.set_index(["Name", "Year", "Month"])
