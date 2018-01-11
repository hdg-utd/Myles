import json
import urllib.request, urllib.parse

def GoogleSearch(term):
    term = urllib.parse.quote_plus(term)
    api_url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBFd__gpNq8mfZkGEcGX2hxA-mN0vCF8b0&cx=005739349085923553089:drmxphvmqfs&q=' + term
    try:
        req = urllib.request.Request(api_url)
        response = urllib.request.urlopen(req)
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        json_response = json.loads(data.decode(encoding))
        print(json_response["items"][0]["displayLink"])
        return json_response["items"][0]["displayLink"]
    except:
        print("none")
        return "none"
