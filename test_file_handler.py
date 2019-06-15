import unittest
import os
import shutil
from scraper_program.file_handler import create_content_file, create_project_directory, create_overview_files, create_file, add_md_formatting

class Test_File_Handler(unittest.TestCase):

    # Test if project directory is being created
    def test1_create_project_directory(self):
        directory = 'elective_dummy'
        create_project_directory(directory) # testing this method
        is_created = False
        if os.path.exists(directory):
            is_created = True
        self.assertTrue(is_created)
    
    # Test if data files are correctly created
    def test2_create_data_files(self):
        project_name = 'elective_dummy'
        base_url = 'https://clbokea.github.io/exam/'
        queue = project_name + "/queue.txt"
        scraped = project_name + "/scraped.txt"

        is_created_queue = False
        is_created_scraped = False

        create_overview_files(project_name, base_url) # testing this method

        if os.path.exists(queue):
            is_created_queue = True
        if os.path.exists(scraped):
            is_created_scraped = True
        self.assertTrue(is_created_queue, 'did not create file: ' + queue)
        self.assertTrue(is_created_scraped, 'did not create file: ' + scraped)
        
    # Test if writefile behaves as intended
    def test3_write_file(self):
        project_name = 'elective_dummy'
        content = project_name + "/content.md"
        path = content
        data = 'this is some test data'

        create_file(path, data) # testing this method
        
        f = open(path, "r")
        resultData = f.read()
        f.close()
        self.assertEqual(resultData, data, 'did not write correctly to file, expected: ' + data + ' got: ' + data)

    # Test if tags are correctly formatted to md
    def test4_add_md_formatting(self):
        contents = []

        # h1 & h2 test
        header1Tag = 'h1im a header tag'
        header1TagResult = '# im a header tag\n'
        header2Tag = 'h2im a header2 tag'
        header2Tag_result = '\n## im a header2 tag\n'

        # p tag test
        ptag = 'pim a p tag'
        ptag_result = 'im a p tag  '

        # p tags to ignore
        p_tag_pNote = 'pNote im a pNote tag'
        p_tag_pAssignment = 'pAssignment im a pAssignment'
        p_tag_pre = 'preIm a pre tag'
        p_tag_pHashtag = 'p#Im a p#'

        # li tag test
        litag = 'liim a li tag'
        litag_result = '\n* im a li tag'
        
        # a tag test        
        atag = 'aim a a tag'
        atag_result = 'im a a tag'

        # Append tests to list
        contents.append(header1Tag)
        contents.append(header2Tag)
        contents.append(ptag)
        contents.append(litag)
        contents.append(atag)
        contents.append(p_tag_pNote)
        contents.append(p_tag_pAssignment)
        contents.append(p_tag_pre)
        contents.append(p_tag_pHashtag)

        # Format the list to md
        formatted_list = add_md_formatting(contents)

        # Run the tests
        self.assertEqual(formatted_list[0], header1TagResult, 'did not format correctly. \nExpected: ' + header1TagResult + '\nGot: ' + contents[0])
        self.assertEqual(formatted_list[1], header2Tag_result, 'did not format correctly. \nExpected: ' + header2Tag_result + '\nGot: ' + contents[1])
        self.assertEqual(formatted_list[2], ptag_result, 'did not format correctly. \nExpected: ' + ptag_result + '\nGot: ' + contents[2])
        self.assertEqual(formatted_list[3], litag_result, 'did not format correctly. \nExpected: ' + litag_result + '\nGot: ' + contents[3])
        self.assertEqual(formatted_list[4], atag_result, 'did not format correctly. \nExpected: ' + atag_result + '\nGot: ' + contents[4])
        self.assertNotIn(p_tag_pNote, formatted_list, 'did not format correctly. \nThis item: ' + p_tag_pNote + '\nShould not be added to the list.')
        self.assertNotIn(p_tag_pAssignment, formatted_list, 'did not format correctly. \nThis item: ' + p_tag_pAssignment + '\nShould not be added to the list.')
        self.assertNotIn(p_tag_pre, formatted_list, 'did not format correctly. \nThis item: ' + p_tag_pre + '\nShould not be added to the list.')
        self.assertNotIn(p_tag_pHashtag, formatted_list, 'did not format correctly. \nThis item: ' + p_tag_pHashtag + '\nShould not be added to the list.')
        shutil.rmtree("elective_dummy") # Delete test dirs to keep project clean    

if __name__ == '__main__':
    unittest.main()