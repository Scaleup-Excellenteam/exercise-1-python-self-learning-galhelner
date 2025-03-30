"""
Week 5 Ex 1 - no_vinnigrette
"""
import datetime
import random


def convert_date(date):
    """Convert a string to date object.

    Args:
        date (str): string represent a date that should be convert.

    Returns:
        date: converted date object (or None if the conversion failed).
    """
    try:
        # trying to convert the given date string based on format template
        valid_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return valid_date
    except ValueError:
        # date convertion failed
        return None


def is_valid_dates(start_date, end_date):
    """Check if two date objects of a date range (start, end) are valid.

    Args:
        start_date (date): start date of the range.
        end_date (date): end date of the range.

    Returns:
        bool: True if the dates are valid, otherwise False.
    """
    invalid_format_msg = "Please enter a valid date format (YYYY-MM-DD)!"
    invalid_date_range_msg = "Start date must be before end date!"

    # make sure dates converted successfully (valid format)
    if start_date is None or end_date is None:
        print(invalid_format_msg)
        return False

    # make sure start date is before end date
    if (end_date - start_date).days < 0:
        print(invalid_date_range_msg)
        return False

    # everything is ok!
    return True


def get_random_date(start_date, end_date):
    """Generate a random date object that is between starting date and ending date.

    Args:
        start_date (date): start date of the range.
        end_date (date): end date of the range.

    Returns:
        date: a random date object in the given date range.
    """
    # calculate a random number of days between start and end dates
    days_delta = (end_date - start_date).days
    random_days_count = random.randint(0, days_delta)
    # calculate and return the random date
    return start_date + datetime.timedelta(days=random_days_count)


def is_monday(date):
    """Check if the day of a date object is monday.

    Args:
        date (date): date to check its day.

    Returns:
        bool: True if the day of the date object is monday, otherwise False.
    """
    return date.weekday() == 0


def get_user_dates():
    """Get the date range objects (end, start) from the user.

    Returns:
        tuple: A topule of 2 date objects based on the user input (start, end).
    """
    while True:
        # read date strings from the user
        start_date_string = input("Enter start date(YYYY-MM-DD):")
        end_date_string = input("Enter end date(YYYY-MM-DD):")

        # convert date strings to date objects
        start_date = convert_date(start_date_string)
        end_date = convert_date(end_date_string)

        # dates validation
        if not is_valid_dates(start_date, end_date):
            continue
        return start_date, end_date


def no_vinnigrete(starting_date, ending_date):
    """Print random date in the range of argument dates, 
    and print no vinnigrette if the random  date is monday.

    Args:
        starting_date (str): String of starting date.
        ending_date (str): String of ending date.
    """
    starting_date_obj = convert_date(starting_date)
    ending_date_obj = convert_date(ending_date)
    random_date = get_random_date(starting_date_obj, ending_date_obj)
    prompt = ''
    if is_monday(random_date):
        prompt += "Ain't gettin' no vinaigrette today: "
    prompt += str(random_date)
    print(prompt)


if __name__ == '__main__':
    # get the start and end dates from the user
    starting_date, ending_date = get_user_dates()

    # get a random date in the range between them
    random_date = get_random_date(starting_date, ending_date)

    # print the random date
    print("Random date:", random_date.date())

    # if the random day is monday im sorry but no vinaigrette today )=
    if is_monday(random_date):
        print("No Vinaigrette!")
