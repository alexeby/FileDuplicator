import random
from datetime import datetime, timedelta


def get_random_date(start_date: datetime, end_date: datetime):
    time_between_dates = end_date - start_date
    seconds_between_dates = time_between_dates.total_seconds()
    random_number_of_seconds = random.uniform(0.0, seconds_between_dates)

    return start_date + timedelta(seconds=random_number_of_seconds)


def random_date_generator(date_format: str, start_date: str, end_date: str):
    if start_date == 'NOW':
        start = datetime.now()
    elif start_date == '01/01/1970':
        start = datetime.strptime(start_date, '%m/%d/%Y')
    else:
        start = datetime.strptime(start_date, date_format)

    end = datetime.now() if end_date == 'NOW' else datetime.strptime(end_date, date_format)
    return get_random_date(start, end).strftime(date_format)
