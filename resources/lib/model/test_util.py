import os
import time
import unittest
import urllib2

def get_HTML(url):
    return urllib2.urlopen(url).read()

EXCLUDE_RATE_LIMITED = os.environ.get('EXCLUDE_RATE_LIMITED') != 'false'

skip_ted_rate_limited = unittest.skipIf(EXCLUDE_RATE_LIMITED, 'Minimal TED website requests.')

__cache__ = {}

class CachedHTMLProvider:

    def get_HTML(self, url):
        '''
        Avoid the wrath of TED by caching requests as much as possible.
        '''
        if url not in __cache__:
            __cache__[url] = get_HTML(url)
            # Aggressive TED rate limiting :'(
            if not EXCLUDE_RATE_LIMITED:
                time.sleep(15)
            else:
                time.sleep(10)
        return __cache__[url]
