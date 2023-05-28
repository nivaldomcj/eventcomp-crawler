CATEGORY_EVENT_URLS_SELECTOR = \
    'a[href^="/cfp/servlet/event.showcfp"]::attr("href")'

CATEGORY_NEXT_PAGE_SELECTOR = \
    'a:contains("next")::attr("href")'

EVENT_TITLE_SELECTOR = \
    'meta[name="description"]::attr("content")'
EVENT_TYPE_SELECTOR = \
    'span[property="v:eventType"]::attr("content")'
EVENT_START_AT_SELECTOR = \
    'span[property="v:startDate"]::attr("content")'
EVENT_FINISH_AT_SELECTOR = \
    'span[property="v:endDate"]::attr("content")'
EVENT_LOCATION_SELECTOR = \
    'span[property="v:locality"]::attr("content")'
EVENT_WEBSITE_SELECTOR = \
    'tr > td > a[target="_newtab"]::attr("href")'
EVENT_CATEGORIES_SELECTOR = \
    'a[href^="../call?conference="]'
EVENT_METADATA_SELECTOR = \
    'tr[valign="middle"] > td[align="center"] > .gglu > tr'
EVENT_DESCRIPTION_SELECTOR = \
    'div.cfp:first-of-type'
