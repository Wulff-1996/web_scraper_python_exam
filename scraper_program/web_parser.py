from html.parser import HTMLParser
from urllib import parse

class WebParser(HTMLParser):

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url                                        # Base url to append href values to
        self.is_inside_article = False                                  # Trigger bool for grapping data
        self.urls = set()                                               # Set for storing unique urls
        self.data = []                                                  # List for data storage
        self.tags = []                                                  # List for tag storage

    def error(self, message):
        return super().error(message)

    # This handles all starttags of the html page
    def handle_starttag(self, tag, attrs):
        if tag == "a":                                                  # If tag is a link
            for (attribute, value) in attrs:                
                if (attribute == "href" 
                and value != "#menu" 
                and value != "next.html"
                and value != "black_jack_pics.html"):
                        url = parse.urljoin(self.base_url, value)       # Join href value with base url                                              
                        self.urls.add(url)                              # Add the complete url to set 
        
        if self.is_inside_article:                                      # If inside article tags i.e between two article tagd
            if tag != "ul":
                self.tags.append(tag)                                   # Append tag to list

        if tag != "article":
            return                                                      # Else dont append
        else:
            self.is_inside_article = True

    # This handles all endtags in the html page            
    def handle_endtag(self, tag):
        if tag == "article" and self.is_inside_article:                 # If end of article tag has been reached
            self.is_inside_article = False                              # Set false        

    # This handles all data between tags in the html page
    def handle_data(self, data):
        if self.is_inside_article:                                      # If between article tags
            self.data.append(" ".join(data.split()))                    # Append data but split whitespace                 

    def get_page_urls(self) -> set():
        return self.urls
    
    # Combines tag & data into a single list, where tags matches the data entries
    def get_data_with_tags(self) -> []:
        data_with_tags = []
        self.data = list(filter(lambda name: name.strip(), self.data))  # Strip all indexes with only whitespaces
        i = 0
        while i < len(self.data):
            tag = self.tags[i]
            data = self.data[i]
            data_with_tags.append(tag + data)
            i += 1
        return data_with_tags