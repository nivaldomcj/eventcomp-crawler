
from bs4 import BeautifulSoup


def html_to_text(description):
    if not description:
        return ''
    if isinstance(description, list):
        description = ''.join(description)

    soup = BeautifulSoup(description, 'html.parser')
    return soup.get_text(separator='\n', strip=True)
