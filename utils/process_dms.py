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
    # cycle on the Description column
    for _, row in dms.iterrows():
        value = row["Description"]
        # there should be an year, if not parsing fails
        try:
            year = pat_year.search(value).group()
        except AttributeError:
            print(f"{value} could not be parsed")
            continue

        # there should be a month, if not, parsing fails
        found = False
        for month in months:
            if month in value:
                found = True
                break
        if not found:
            print(f"{value} could not be parsed")
            continue

        for string in [dummy_tag, month, year]:
            value = value.replace(string, "")
        name = value.strip()
        rows.append(
            {"Name": name, "Month": month, "Year": year, "DMS": row["Reference"]}
        )

    dms_new = pd.DataFrame(rows)
    return dms_new.set_index(["Name", "Year", "Month"])
