import unittest
from url_shortener import URLShortener

class URLShortenerTest(unittest.TestCase):

    def test_encode_url(self):
        sut = URLShortener()

        rowId = 125
        expected = "cb" 
        actual = sut.encode_url(rowId)

        self.assertEqual(expected, actual)

    def test_encode_url2(self):
        sut = URLShortener()

        rowId = 19158 
        expected = "e9a" 
        actual = sut.encode_url(rowId)

        self.assertEqual(expected, actual)

    def test_decode_url(self):
        sut = URLShortener()

        url = "cb" 
        expected = 125
        actual = sut.decode_url(url)

        self.assertEqual(expected, actual)

    def test_decode_url2(self):
        sut = URLShortener()

        url = "e9a" 
        expected = 19158 
        actual = sut.decode_url(url)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
