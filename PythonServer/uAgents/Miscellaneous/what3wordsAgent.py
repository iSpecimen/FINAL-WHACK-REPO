import requests
import json
from uagents import Agent, Bureau, Context, Model

# scrapes the json file from opencage and gets the w3w for coordinates
def get_words(lat: int, long:str):
    key = "b356e3592e8342cbbd7ab0bcb73db0e3"
    website = "https://api.opencagedata.com/geocode/v1/json?q="+str(lat)+"%2C"+str(long)+"&"+"key="+key
    scraped = requests.get(website)
    data = scraped.text
    parsed = json.loads(data)
    words = parsed["results"][0]["annotations"]["what3words"]["words"]
    return words


MASTER = ""

# Defines the message
class Message(Model):
    lat: str
    long:str
    words: str

# Defines agent
what3words = Agent(
    name="what3words",
    port=8001,
    seed="What3WordsRecovery",
    endpoint=["http://127.0.0.1:8001/submit"],
    mailbox="91f41dff-a202-4b6b-a75a-68b9524b648e",
)

#get latitude/longitude here
latitude = ""
longitude = ""

MASTER = ""

"""
WHAT3WORDS = ""
class Message(Model):
    lat: str
    long:str
    words: str


@master.on_message(model=Message)
async def receive_words(ctx:Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.words}")
    words = msg.words

    await ctx.send(WHAT3WORDS, Message(lat=latitude, long=longitude, words="None"))
    

"""

# Receives the lat and long values from master
@what3words.on_message(model=Message)
async def what3words_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.lat}, {msg.long}")
    word = get_words(msg.lat, msg.long)

# Sends the values
@what3words.on_message(model=Message)
async def send_words(ctx: Context):
    await ctx.send(MASTER, Message(lat="", long="", words=word))


    
    

# Runs the agent
if __name__ == "__main__":
    what3words.run()
    print(what3words.address)

