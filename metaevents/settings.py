import os

from dotenv import load_dotenv

load_dotenv()

# Scrapy settings for metaevents project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "metaevents"

SPIDER_MODULES = ["metaevents.spiders"]
NEWSPIDER_MODULE = "metaevents.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Whether to enable the cookies middleware
COOKIES_ENABLED = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "metaevents.middlewares.MetaeventsSpiderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   "scrapy.extensions.telnet.TelnetConsole": None,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True

# ------------------------------------------------------------------------------

# https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "metaevents.pipelines.MongoDbPipeline": 200,
}

# Set log level for all spiders
LOG_LEVEL = os.getenv('SCRAPY_LOG_LEVEL', 'DEBUG')

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# MongoDB connection
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')

# ------------------------------------------------------------------------------

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
   "scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware": 500,
}

# User agents that will be rotated while spider is fetching pages
# See https://www.whatismybrowser.com/guides/the-latest-user-agent/
USER_AGENTS = [
   # Android
   ('Mozilla/5.0 (Linux; Android 13) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Linux; Android 13; SM-A205U) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Linux; Android 13; SM-A102U) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Linux; Android 13; SM-G960U) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Linux; Android 13; SM-N960U) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Simage.pngafari/537.36'),  # Chrome
   ('Mozilla/5.0 (Linux; Android 13; LM-Q720) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Linux; Android 13; LM-X420) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Linux; Android 13; LM-Q710(FGN)) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.5672.162 Mobile '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Android 13; Mobile; rv:68.0) '
    'Gecko/68.0 '
    'Firefox/113.0'),  # Firefox
   ('Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:113.0) '
    'Gecko/113.0 '
    'Firefox/113.0'),  # Firefox

   # Windows
   ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 Safari/537.36 '
    'Edg/113.0.1774.57'),  # Edge
   ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Windows NT 10.0) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 '
    'Safari/537.36'),  # Chrome
   ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) '
    'Gecko/20100101 '
    'Firefox/113.0'),  # Firefox
   ('Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 Safari/537.36 '
    'Vivaldi/6.0.2979.18'),  # Vivaldi
   ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 Safari/537.36 '
    'Vivaldi/6.0.2979.18'),  # Vivaldi


    # MacOS
   ('Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) '
    'AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'Version/16.5 Safari/605.1.15'), # Safari
   ('Mozilla/5.0 (Macintosh; Intel Mac OS X 13.4; rv:113.0) '
    'Gecko/20100101 '
    'Firefox/113.0'), # Firefox
   ('Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 '
    'Safari/537.36'), # Chrome
   ('Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 Safari/537.36 '
    'Vivaldi/6.0.2979.18'), # Vivaldi 	
   ('Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/113.0.0.0 Safari/537.36 '
    'Edg/113.0.1774.57'), # Edge

   # iOS
   ('Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) '
    'AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'Version/16.5 Mobile/15E148 '
    'Safari/604.1'), # Safari
   ('Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) '
    'AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'CriOS/113.0.5672.121 Mobile/15E148 '
    'Safari/604.1'), # Chrome
   ('Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) '
    'AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'FxiOS/113.0 Mobile/15E148 '
    'Safari/605.1.15'), # Firefox

   # ChromeOS
   ('Mozilla/5.0 (X11; CrOS x86_64 15359.58.0) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/112.0.5615.134 '
    'Safari/537.36'),
   ('Mozilla/5.0 (X11; CrOS armv7l 15359.58.0) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/112.0.5615.134 '
    'Safari/537.36'),
   ('Mozilla/5.0 (X11; CrOS aarch64 15359.58.0) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/112.0.5615.134 '
    'Safari/537.36'),
   ('Mozilla/5.0 (X11; CrOS x86_64 15359.58.0) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/112.0.5615.134 '
    'Safari/537.36'),
   ('Mozilla/5.0 (X11; CrOS armv7l 15359.58.0) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/112.0.5615.134 '
    'Safari/537.36'),
   ('Mozilla/5.0 (X11; CrOS aarch64 15359.58.0) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/112.0.5615.134 '
    'Safari/537.36'),
]