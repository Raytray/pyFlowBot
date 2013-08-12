import urllib
import flowdock
import ConfigParser
import requests
import json

from flowdock import JSONStream

config = ConfigParser.ConfigParser()
config.read('apikey.cfg')

FLOW_API_KEY = config.get('DEFAULT', 'FLOW_API_KEY')

CAT_URL = "http://thecatapi.com/api/images/get?format=src&type=gif"

def get_gif():
    gif_url = requests.get(CAT_URL)
    return gif_url.url

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
