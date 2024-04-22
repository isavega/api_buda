import datetime
import pytz
import locale

def format_number_to_CLP(number):
    number_str = str(number)
    integer_part, decimal_part = number_str.split('.')
    formatted_integer = '{:,}'.format(int(integer_part)).replace(',', '.')
    formatted_number = f"${formatted_integer},{decimal_part}"
    return formatted_number

def calculate_traded_money(entries):
    buys = 0
    sells = 0
    buy="buy"

    for entry in entries:
        if entry[3] == buy:
            buys += float(entry[1]) * float(entry[2])
        else:
            sells += float(entry[1]) * float(entry[2])

    traded_money = buys + sells
    return round(traded_money, 2)

def convert_to_milliseconds(start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute, timezone_str):

    start = datetime.datetime(start_year, start_month, start_day, start_hour, start_minute)
    end = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute)

    timezone = pytz.timezone(timezone_str)

    start_with_timezone = timezone.localize(start)
    end_with_timezone = timezone.localize(end)

    # Get the Unix timestamps in seconds for start and end
    timestamp_start_seconds = int(start_with_timezone.timestamp())
    timestamp_end_seconds = int(end_with_timezone.timestamp())

    # Convert the timestamps to milliseconds
    timestamp_start_milliseconds = timestamp_start_seconds * 1000
    timestamp_end_milliseconds = timestamp_end_seconds * 1000

    return timestamp_start_milliseconds, timestamp_end_milliseconds




