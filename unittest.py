import unittest


class WebCrawling(unittest.TestCase):
    headers = {'User-Agent': 'Mobile'}
    url2 = 'http://httpbin.org/headers'
    rh = requests.get(url2, headers=headers)
    print(rh.text)

    def test_headers(self):
        self.assertTrue(TestingHeader.headers, 'Mobile')


if name == 'main':
        unittest.main()


