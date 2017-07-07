import os
import unittest
import urllib2

def get_HTML(url):
    return urllib2.urlopen(url).read()
    

class CachedHTMLProvider:

    __cache__ = {}

    def get_HTML(self, url):
        if url not in self.__cache__:
            self.__cache__[url] = get_HTML(url)
        return self.__cache__[url]

skip_ted_rate_limited = unittest.skipIf(os.environ.get('EXCLUDE_RATE_LIMITED') != 'false', 'Minimal TED website requests.')
