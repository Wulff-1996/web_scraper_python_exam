# Python Web Crawler

This repository contains the source code solution to the first exam assignment in the python elective at KEA's computer science course. See project description and install instructions below.  

### Project Description
The requirements for this assignment, was to build a program capable of "crawling & scraping" the contents of a website and saving the content from each individual site into locally stored .md files without the use of any third party modules. The advice was to choose a small website and also get some sort of limit on how many links should be followed.

### Project Outline
This program is built to specifically target at dummy website setup by the teacher in order to keep the scope and magnitude of the assignment to a managable level.   
The main actor in the program is the "scraper.py" module, which uses a combination of Python's built in modules to solve the task at hand. The html content from the dummy site is retrieved using urllib.request which is then passed to a custom subclassed HTMLParser that extracts the content and links from each site. The scraper then passes this to a custom filehandler module, which formats and writes it to individual files. To ensure the same link is never scraped twice, each time a link has been scraped, the scraper will add it to a "scraped.txt" file and likewise add new links to a "queue.txt" file. To restrict the amount of pages scraped, the program will only go to links if it contain a specified domain name, if it doesn't the program will not add it to the queue and simply ignore it. The program will also crate the necessary files and directories if they don't already exist, using the os module.

### Project Install
Since no thrid party modules were used for this project, it is possible to run it with no required setup as long as you are using Python 3.5+. Simply clone the repository.

### Project run
**To execute the main program:**  
1. Navigate to "scraper_program" directory in the cloned repo.
2. Execute "main.py" from terminal.
3. You should see prints in terminal informing wether the program was successful or not. 
4. The contents from the scraped websites will be located in a new directory at "/scraper_program/elective_dummy/"

**To execute the tests:**  
1. Navigate to cloned repo.
2. Execute either "test_file_handler.py" or "test_web_parser.py"
3. You should see prints in terminal informing of test results. 


***Programmers:*** *Christian Skydt & Jakob Wulff*
