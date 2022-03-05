import requests

url = 'https://www.logitechg.com/en-sg/products/gaming-audio.html'

r = requests.get(url)

print(r.text)

print("Status Code:")

print("\t*",r.status_code)

h = requests.head(url)

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent' :'Mobile'
}

url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

import scrapy

class AudioSpider(scrapy.Spider):
    name = "New_Audio"
    start_urls = [
        'https://www.logitechg.com/en-sg/products/gaming-audio.html'
    ]

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

        # Task 7
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
# Importing appropriate libraries
import unittest

# Task 8
class TestingHeader(unittest.TestCase):
    headers = {'User-Agent': 'Mobile'}
    url2 = 'http://httpbin.org/headers'
    rh = requests.get(url2, headers=headers)
    print(rh.text)

    def test_headers(self):
        self.assertTrue(TestingHeader.headers, 'Mobile')

if __name__ == '__main__':
    unittest.main()