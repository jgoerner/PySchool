import requests

def get_source_code(URL, protocol="http"):
    """
    Return the raw source code of a website
    """
    query_URL = protocol + "://" + URL
    result = requests.get(query_URL)
    return result.text

if __name__ == "__main__":
    print("starting")
    text = get_source_code("www.ietf.org/rfc.html")
    print("done")
    print(text)
