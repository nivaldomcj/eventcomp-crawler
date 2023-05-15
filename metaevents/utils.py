from re import sub


def to_snake_case(string):
    if not string:
        return ''
    return (
        '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
                sub('([A-Z]+)', r' \1',
                    string.replace('-', ' '))).split()).lower()
    )
