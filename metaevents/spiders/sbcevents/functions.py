import dateparser


def parse_sbc_event_title(titles_found):
    for title in titles_found:
        if title is not None:
            return title.strip()
    return ''


def parse_sbc_event_date(event_dates, finish_at=False):
    if event_dates:
        if finish_at:
            date_string = event_dates[1] if len(event_dates) > 1 else None
        else:
            date_string = event_dates[0] if len(event_dates) > 0 else None

        if date_string:
            # <= 'De\xa0Quinta-feira, 30 Março 2023'
            # => ['De', 'Quinta-feira, 30 Março 2023']
            date_string = date_string.split('\xa0')[-1]
            return dateparser.parse(date_string) if date_string else None
    return None
