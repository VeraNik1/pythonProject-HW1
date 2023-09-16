def _is_leap_year(year: int) -> bool:
    """function to check if the year is leap.
    It returns True if the year is leap and False if it's not """

    if not year % 400:
        return True
    elif not year % 4 and year % 100:
        return True
    return False


def date_exists(date: tuple | list) -> bool:
    """function takes tuple/list of integers: date in format [YYYY, (M)M, (D)D]
    and checks if date exists.

    Returns True if the date exists

    Returns False if it doesn't
    """
    year, month, day = date
    if year > 9999 or year < 1 or month > 12 or month < 1 or day > 31 or day < 1:
        return False
    if month in (1, 3, 5, 7, 8, 10, 12) and day < 32:
        return True
    elif month in (4, 6, 9, 11) and day < 31:
        return True
    elif _is_leap_year(year) and month == 2 and day < 30:
        return True
    elif not _is_leap_year(year) and month == 2 and day < 29:
        return True
    return False


def make_date_list_from_string(date_str: str):
    """ converts date in string format to the list like [YYYY, (M)M, (D)D]"""
    result = None
    delimiters = ('.', '\\', '/', ',', ':', '-')
    for item in delimiters:
        if item in date_str:
            try:
                result = list(map(int, date_str.split(item)))
            except:
                break

    return result
