import urllib
import flowdock
import ConfigParser
import requests
import json

from flowdock import JSONStream


config = ConfigParser.ConfigParser()
config.read('apikey.cfg')

API_KEY = config.get('DEFAULT', 'API_KEY')
FLOW_API_KEY = config.get('DEFAULT', 'FLOW_API_KEY')
TUMBLR_URL = 'http://api.tumblr.com/v2/'


def get_gif():
    params = [('tag', 'gif'), ('api_key', API_KEY)]
    res_url = "{}tagged/?{}".format(TUMBLR_URL, urllib.urlencode(params))

    response = requests.get(res_url)

    json_response = json.loads(response.text)
    # TODO make random

    return json_response['response'][0]['photos'][0]['original_size']['url']


def process_data(data):
    print data["content"]
    # TODO match keyword


def send_gif(url):
    pass
    # TODO impersonate you
    # and send back

def main():
    stream = JSONStream(FLOW_API_KEY)
    gen = stream.fetch(['parsely/eng-interns'])
    for data in gen:
        if type(data) == dict and data["event"] == "message":
            process_data(data)


if __name__ == "__main__":
    main()
