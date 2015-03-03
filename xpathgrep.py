#!/usr/bin/python
import sys
import urllib2
from scrapy.selector import Selector    # tested with scrapy 0.20.2

def xpathgrep(xpath, url):
    with urllib2.urlopen(url) as page_handle:
        html_source = page_handle.read()
    selector = Selector(text=html_source)
    return '\t'.join(selector.xpath(xpath).extract())

if __name__=='__main__':
    xpath = sys.argv[1]
    url = sys.argv[2]
    print xpathgrep(xpath, url)
