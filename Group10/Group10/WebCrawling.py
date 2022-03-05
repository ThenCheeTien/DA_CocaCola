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