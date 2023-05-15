import dateparser


def parse_resurchify_date(date_string, finish_at=False):
    if date_string:
        if isinstance(date_string, list):
            date_string = date_string.pop() if len(date_string) else ''
        date_string = date_string.split(' - ')

        if finish_at:
            date_string = date_string[1] if len(date_string) > 1 else None
        else:
            date_string = date_string[0] if len(date_string) > 0 else None

        if date_string:
            return dateparser.parse(date_string) if date_string else None
    return None
