from re import sub
import dateparser


def to_snake_case(string):
    if not string:
        return ''
    return (
        '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
                sub('([A-Z]+)', r' \1',
                    string.replace('-', ' '))).split()).lower()
    )


def parse_field_title(string):
    if not string:
        return None
    return sub(r'[^a-zA-Z_0-9]+', '', to_snake_case(string))


def parse_field_value(value):
    if isinstance(value, str):
        value = value.strip()

    try:
        return int(value)
    except:
        pass
    try:
        return dateparser.parse(value)
    except:
        pass

    return value
