from urllib.request import urlopen
from web_parser import WebParser
from file_handler import create_project_directory, create_overview_files, create_content_file, set_to_file, list_to_file, file_to_set
from domain_formatter import get_path_name
import sys
import os

class Scraper:

    def __init__(self, project_name, base_url, domain_name):
        self.project_name = project_name                                                            # Name of the project directory
        self.base_url = base_url                                                                    # Name of the first website to scrape    
        self.domain_name = domain_name                                                              # All URLs must contains this name to be searched            
        self.queue_file = project_name + "/queue.txt"                                               # File containing urls to scrape        
        self.scraped_file = project_name + "/scraped.txt"                                           # File containing scraped urls    
        self.data_list = []                                                                         # List for storing website data    
        self.queue = set()                                                                          # Set for processing queued urls
        self.scraped = set()                                                                        # Set to avaoid processing same urls   
        self.start_up()                                                                             # Setup scraper and project dirs/files
        self.scrape_page(self.base_url, project_name + "/" + get_path_name(base_url) + ".md" )      # Scrape initial page (base_url)        

    def start_up(self):
        create_project_directory(self.project_name)
        create_overview_files(self.project_name, self.base_url)
        self.queue = file_to_set(self.queue_file)                                                   # Convert file to set for faster processing
        self.scraped = file_to_set(self.scraped_file)                                            
        print("-- Scraper initialised --")

    def scrape_page(self, page_url, path):
        if page_url not in self.scraped:
            create_content_file(path)                                                               # Created here since each name must be unique
            self.add_links_to_queue(self.collect_links_and_data(page_url))                          # Add new links to queue
            self.queue.remove(page_url)                                                             # Remove current url from queue
            print("Scraping: " + page_url)
            print("Queue: " + str(len(self.queue)) + " | Scraped: " + str(len(self.scraped)))
            self.scraped.add(page_url)                                                              # Add scraped page to set
            self.update_files(path)                                                                 # Update all project files

    # Collects all urls and data from specified website
    def collect_links_and_data(self, page_url):
        try:
            html_string = ""
            response = urlopen(page_url)
            if "text/html" in response.getheader("Content-Type"):                                   # Check to see if HTML response
                html_bytes = response.read()                                                        # Read the bytestream in response
                html_string = html_bytes.decode("utf-8")                                            # Decode bytestream as utf-8
            
            parser = WebParser(self.base_url)                                                       # Initialise custom webparser with html response
            parser.feed(html_string)                                                                # Execute parser    
            self.data_list = parser.get_data_with_tags()                                            # Retrieve datalist from parser
        except Exception as e:
            print("Error: " + str(e))
            print("Program will terminate")
            sys.exit()
        return parser.get_page_urls()
    
    # Add urls to queue depending on conditions
    def add_links_to_queue(self, links) -> None:                                                           
        for url in links:
            if url in self.queue:
                continue
            if url in self.scraped:
                continue
            if self.domain_name not in url:                                                         # Only add urls that are in the domain
                continue
            self.queue.add(url)

    # Called every time a website has been scraped
    def update_files(self, path):
        set_to_file(self.queue, self.queue_file)
        set_to_file(self.scraped, self.scraped_file)
        list_to_file(self.data_list, path)