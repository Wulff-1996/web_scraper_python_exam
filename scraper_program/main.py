from scraper import Scraper
from domain_formatter import get_domain_name, get_sub_domain_name, get_path_name
from file_handler import file_to_set

PROJECT_NAME = "elective_dummy"
HOMEPAGE = "https://clbokea.github.io/exam/index.html"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
content_file = PROJECT_NAME + "/content"

# Initialise scraper to scrape initial site & add links to queue file
scraper = Scraper(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Use scraper to scrape every url in queue file
def run():
        queue_urls = file_to_set(QUEUE_FILE)

        for url in queue_urls:
                scraper.scrape_page(url, PROJECT_NAME + "/" + get_path_name(url) + ".md")
        check_queue()

# This will ensure the queuefile is empty after running, 
# in case new links were added during run
def check_queue():
        if len(file_to_set(QUEUE_FILE)) > 0:
                run()
        else:
                print("-- All pages from '" + get_sub_domain_name(HOMEPAGE) + "' was scraped --")

run()