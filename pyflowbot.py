import urllib
import flowdock
import ConfigParser
import requests
import json

config = ConfigParser.ConfigParser()
config.read('apikey.cfg')

API_KEY = config.get('DEFAULT', 'API_KEY')
TUMBLR_URL = 'http://api.tumblr.com/v2/'


def get_gif():
    params = [('tag', 'gif'), ('api_key', API_KEY)]
    res_url = "{}tagged/?{}".format(TUMBLR_URL, urllib.urlencode(params))

    response = requests.get(res_url)

    json_response = json.loads(response.text)

    return json_response['response'][0]['photos'][0]['original_size']['url']


def main():
    print get_gif()


if __name__ == "__main__":
    main()
