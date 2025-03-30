import datetime
import random


def convert_date(date):
    try:
        # trying to convert the given date string based on format template
        valid_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return valid_date
    except ValueError:
        # date convertion failed
        return None


def is_valid_dates(start_date, end_date):
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
    # calculate a random number of days between start and end dates
    days_delta = (end_date - start_date).days
    random_days_count = random.randint(0, days_delta)
    # calculate and return the random date
    return start_date + datetime.timedelta(days=random_days_count)


def is_monday(date):
    return date.weekday() == 0


def get_user_dates():
    while True:
        # read date strings from the user
        start_date = input("Enter start date(YYYY-MM-DD):")
        end_date = input("Enter end date(YYYY-MM-DD):")

        # convert date strings to date objects
        start_date = convert_date(start_date)
        end_date = convert_date(end_date)

        # dates validation
        if not is_valid_dates(start_date, end_date):
            continue
        return start_date, end_date


if __name__ == '__main__':
    # get the start and end dates from the user
    start_date, end_date = get_user_dates()

    # get a random date in the range between them
    random_date = get_random_date(start_date, end_date)

    # print the random date
    print("Random date:", random_date.date())

    # if the random day is monday im sorry but no vinaigrette today )=
    if is_monday(random_date):
        print("No Vinaigrette!")
