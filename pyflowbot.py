import urllib
import flowdock
import ConfigParser
import requests
import json

from flowdock import JSONStream

from flowdock import Chat


config = ConfigParser.ConfigParser()
config.read('apikey.cfg')

FLOW_API_KEY = config.get('DEFAULT', 'FLOW_API_KEY')
FLOW_TOKEN = config.get('DEFAULT' , 'FLOW_TOKEN' )

CAT_URL = "http://thecatapi.com/api/images/get?format=src&type=gif"

def get_gif():
    gif_url = requests.get(cat_url)
    return gif_url.url
    #print gif_url

def process_data(data):
    matching_word = "should"
    data_of_flow = data["content"]
    #print data_of_flow.find("should")
    if data_of_flow.find("should") != -1:
        send_gif(CAT_URL)


def send_gif(CAT_URL):
    chat = Chat(FLOW_TOKEN)
    chat.post(CAT_URL , 'Raymond')
    pass

def main():
    stream = JSONStream(FLOW_API_KEY)
    gen = stream.fetch(['parsely/eng-interns'])
    for data in gen:
        if type(data) == dict and data["event"] == "message":
            process_data(data)


if __name__ == "__main__":
    main()
