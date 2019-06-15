from urllib.parse import urlparse

# Get domain name (github.io)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split(".")
        return results[-2] + "." + results[-1]
    except:
        return ""


# Get sub domain name (clbokea.github.io)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ""

# Get path name (index)
def get_path_name(url):
    try:
        result = urlparse(url).path.split("/")
        return result[-1].replace(".html", "")
    except:
        return ""