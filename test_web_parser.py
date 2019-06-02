import unittest
from scraper_program.web_parser import WebParser

class Test_Web_Parser(unittest.TestCase):

     def test_get_data_with_tags(self):
        data_one = 'this is data one'
        data_two = 'this is data two'
        data_three = 'this is data three'
        data_four = '                 '
        data_five = 'sefsefsef'
        data_six = 'sefsefsef'

        tags_one = 'p'
        tags_two = 'a'
        tags_three = 'h1'
        tags_four = 'h2'
        tags_five = 'p'

        finder = WebParser('')
        finder.data.append(data_one)
        finder.data.append(data_two)
        finder.data.append(data_three)
        finder.data.append(data_four)
        finder.data.append(data_five)
        finder.data.append(data_six)
        finder.tags.append(tags_one)
        finder.tags.append(tags_two)
        finder.tags.append(tags_three)
        finder.tags.append(tags_four)
        finder.tags.append(tags_five)

        data_with_tags = finder.get_data_with_tags() ##  testing this method

        self.assertNotIn(data_four, data_with_tags, 'Error: indexes with only whitespaces in list. \nThis object still in list: ' + data_four)
        self.assertTrue(len(finder.data) == len(finder.tags), 'Error: data list and tags list is not the same lenght. \nData list: ' + str(len(finder.data)) + '\nTags list: ' + str(len(finder.tags)))

if __name__ == '__main__':
    unittest.main()