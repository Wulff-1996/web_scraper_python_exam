import unittest
from scraper_program.domain_formatter import get_domain_name, get_sub_domain_name, get_path_name

class Test_domain_formatter(unittest.TestCase):

    url = "http://www.docs.example.com/index.html"

    def test_get_domain_name(self):
        url_result = "example.com"
        self.assertEqual(get_domain_name(self.url), url_result, "did not format url correctly, expected: " + url_result + " got: " + get_domain_name(self.url))


    def test_get_sub_domain_name(self):
        url_result = "www.docs.example.com"
        self.assertEqual(get_sub_domain_name(self.url), url_result, "did not format url correctly, expected: " + url_result + " got: " + get_sub_domain_name(self.url))

    def test_get_path_name(self):
        url_result = "index"
        self.assertEqual(get_path_name(self.url), url_result, "did not format correctly, expacted: " + url_result + " got: " + get_path_name(self.url))

if __name__ == "__main__":
    unittest.main()