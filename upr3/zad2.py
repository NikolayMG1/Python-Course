from datetime import datetime


def format_date_components(year, month, day, separator='-'):

    return f"{year:0>4d}{separator}{month:0>2d}{separator}{day:0>2d}"


assert format_date_components(2023, 10, 22) == '2023-10-22'
assert format_date_components(2112, 12, 21, separator='/') == '2112/12/21'
assert format_date_components(1970, 1, 1) == '1970-01-01', "check your leading zeroes formatting!"
assert format_date_components(1, 12, 25) == '0001-12-25'