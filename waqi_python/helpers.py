from dateutil.parser import parse


def convert_to_datetime(time, tz):
    try:
        return parse(f'{time} {tz}')
    except ValueError:
        return None
