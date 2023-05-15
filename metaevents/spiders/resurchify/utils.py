import dateparser
import re

from metaevents.utils import to_snake_case


def parse_field_title(string):
    if not string:
        return None
    return re.sub(r'[^a-zA-Z_0-9]+', '', to_snake_case(string))


def parse_field_value(string):
    try:
        return int(string)
    except:
        pass
    try:
        return dateparser.parse(string)
    except:
        pass
    return string
