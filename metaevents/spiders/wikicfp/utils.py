from re import findall
from urllib.parse import parse_qs, unquote_plus, urlparse

from metaevents.utils import parse_field_value


def get_category_name(url):
    unquoted_url = unquote_plus(url)
    parsed_url = urlparse(unquoted_url)
    return parse_qs(parsed_url.query)['conference'][0] or None


def get_event_id(url):
    event_id = findall(r'\?eventid=(.+)\&', url)
    return int(event_id.pop()) if event_id and len(event_id) else None


def get_event_dates(value):
    splitted_value = value.split(' - ')
    if len(splitted_value) == 0:
        return (None, None)
    return map(parse_field_value, splitted_value)


def select_field_value(selector):
    from_td = selector.css('td::text').get()
    from_td = from_td.strip() if from_td else ''

    if from_td:
        return from_td

    from_span = selector.css('td > span::text').get()
    from_span = from_span.strip() if from_span else ''

    if from_span:
        return from_span

    for prop in selector.css('td > span > span[property]::text').getall():
        if prop is not None and isinstance(prop, str) and len(prop):
            return prop

    return None
