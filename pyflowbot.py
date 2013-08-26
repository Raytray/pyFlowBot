import flowdock
import ConfigParser
import requests

from flowdock import JSONStream, Chat


config = ConfigParser.ConfigParser()
config.read('apikey.cfg')

FLOW_USER_API_KEY = config.get('DEFAULT', 'FLOW_USER_API_KEY')
FLOW_TOKEN = config.get('DEFAULT' , 'FLOW_TOKEN' )
match_word = {
        "!catgif": "get_gif()",
        "!doggif": "get_gif()"
    }

CAT_URL = "http://thecatapi.com/api/images/get?format=src&type=gif"
Flows_to_fetch = ['parsely/eng-interns', 'parsely/devtalk', 'parsely/parse-ly-sales', 'parsely/main']

def get_gif():
    gif_url = requests.get(CAT_URL)
    return gif_url.url


def process_data(data):
    if data['content'] in match_word:
        print data['flow']
        send_gif(eval(match_word[data['content']]))
        
def send_gif(gif_url):
    chat = Chat(FLOW_TOKEN)
    chat.post(gif_url, 'PyFlowBot')


def main():
    stream = JSONStream(FLOW_USER_API_KEY)
    gen = stream.fetch(Flows_to_fetch)
    for data in gen:
        if type(data) == dict and data['event'] == "message":
            process_data(data)


if __name__ == "__main__":
    main()
