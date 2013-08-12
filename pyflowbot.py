import flowdock
import ConfigParser
import requests
 
from flowdock import JSONStream
 
from flowdock import Chat
 
 
config = ConfigParser.ConfigParser()
config.read('apikey.cfg')
 
FLOW_USER_API_KEY = config.get('DEFAULT', 'FLOW_USER_API_KEY')
FLOW_TOKEN = config.get('DEFAULT' , 'FLOW_TOKEN' )
 
CAT_URL = "http://thecatapi.com/api/images/get?format=src&type=gif"
 
 
def get_gif():
    gif_url = requests.get(CAT_URL)
    return gif_url.url
 
 
def process_data(data):
    matching_word = "!catgif"
    data_of_flow = data["content"]
    if data_of_flow.find("!catgif") != -1:
        send_gif(get_gif())
 
 
def send_gif(gif_url):
   chat = Chat(FLOW_TOKEN)
   chat.post(CAT_URL , 'PyFlowBot')
   pass
 
 
def main():
    stream = JSONStream(FLOW_USER_API_KEY)
    gen = stream.fetch(['parsely/eng-interns'])
    for data in gen:
        if type(data) == dict and data["event"] == "message":
            process_data(data)
 
 
if __name__ == "__main__":
    main()