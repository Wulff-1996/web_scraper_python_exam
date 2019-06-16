from urllib.parse import urlparse

# Get domain name (github.io)
def get_domain_name(url: str) -> str:
    '''returns the domain name of an url, example http://www.example.com/index.html -> example.com'''
    try:
        results = get_sub_domain_name(url).split(".")
        return results[-2] + "." + results[-1]
    except:
        return ""

# Get sub domain name (clbokea.github.io)
def get_sub_domain_name(url: str) -> str:
    '''returns the subdomain name of a url, example http://www.docs.example.com/html -> www.docs.example.com'''
    try:
        return urlparse(url).netloc
    except:
        return ""

# Get path name (index)
def get_path_name(url: str) -> str:
    '''this method returns the path name of a given url, example http://www.example.com/index.html -> index'''
    try:
        result = urlparse(url).path.split("/")
        return result[-1].replace(".html", "")
    except:
        return ""