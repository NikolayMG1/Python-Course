def extract_date_components(str):

    year_str, month_str, day_str = str.split('-')
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    return year, month, day

assert extract_date_components('1970-01-01') == (1970, 1, 1)
assert extract_date_components('2023-10-22') == (2023, 10, 22)
assert extract_date_components('0000-12-25') == (0, 12, 25)
assert extract_date_components('2009-02-29') == (2009, 2, 29)