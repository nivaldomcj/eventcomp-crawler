EVENTS_LIST_ROWS_SELECTOR = \
    'table.w3-table.w3-white > tbody'
EVENT_DETAILS_URL_SELECTOR = \
    'a[href^="https://www.resurchify.com/ed/"]::attr("href")'
EVENT_DETAILS_CATEGORIES_SELECTOR = \
    'tr:nth-child(4) > td > a::attr("href")'
EVENT_LIST_NEXT_PAGE_SELECTOR = \
    'a:contains("Next »")::attr("href")'

EVENT_TITLE_SELECTOR = \
    'h1.heading_h1 > b::text'
EVENT_DATE_SELECTOR = \
    'tr.w3-theme-l4 > td.w3-border::text'
EVENT_LOCATION_SELECTOR = \
    'div.w3-text-gray > b::text'
EVENT_WEBSITE_SELECTOR = \
    '.w3-container > .w3-center > span > a[target="_blank"]::attr("href")'
EVENT_DESCRIPTION_SELECTOR = \
    '//div[@id="Call_for_paper"]/div/div/table/tbody/tr[last()]'
EVENT_CATEGORIES_SELECTOR = \
    '//div[@class="w3-medium "]/b/text()'

EVENT_METADATA_SELECTOR = \
    'table.table1 > tbody > tr'
