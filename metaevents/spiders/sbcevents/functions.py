import dateparser


def parse_sbc_event_title(titles_found):
    for title in titles_found:
        if title is not None:
            return title
    return ''


def parse_sbc_event_date(date_string):
    if not date_string:
        return date_string

    # <= 'De\xa0Quinta-feira, 30 Março 2023'
    # => ['De', 'Quinta-feira, 30 Março 2023']
    date_string = date_string.split('\xa0')[-1]
    parsed_date = dateparser.parse(date_string)
    return parsed_date.date() if parsed_date else None
