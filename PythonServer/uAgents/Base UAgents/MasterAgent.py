#MASTER UAGENT#

from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
import os



#os.system("timingAgent.py")
#os.system("what3Words.py")
#os.system("CarParks.py")
os.system("Weather.py")
CarParkAgentAddress="agent1q2a45mxzld7ffe484ejup3g4mqk83x4hf8qhhl7ratzyh5x3s0kuk6vwqrn"
what3WordsAgentAddress="agent1qfc5uu3mseyrnwwnw675pwve685ysduk36zhtaasw2ad5kar8x67g6fgsdv"
TimingAddress="agent1qfc6pwc8zfru0sf23skfj6r6vtwducm9pvr5435akf9cm8gz7z4vw4tag6e"
WeatherAddress="agent1qvlfvexrf3j0gjskxsr4gm0psmzhhnzzp5v3cxvxj2r66v5kyhqrkymn50v" #old address
# agent1qw49f56dhvu5fmat3hqfngn46t9drnjswwsr3sy37l50nqhdy6wzwllpyaj new address

masterAgent = Agent(
    name="masterAgent",
    port=8000,
    seed="MASTER AGENT",
    endpoint=["http://localhost:8000/submit"],
)

fund_agent_if_low(masterAgent.wallet.address())

class CParkCoords(Model):
    latitude: float
    longitude: float

@masterAgent.on_message(model=CParkCoords)
async def carParks_message_handler(ctx: Context, sender: str, msg: CParkCoords):
    print("Recieved messages")
    ctx.logger.info(f"Received message from {sender}: {msg.latitude}, {msg.longitude}")
    latitude = msg.latitude
    longitude = msg.longitude

    CarParksFile = open("CarParkCoords.txt", "w") 
    CarParksFile.write(latitude)
    CarParksFile.write(longitude)

    CarParksFile.close()



class Timing(Model):
    message : str


class WeatherData(Model):
    conditions: str



class Message(Model):
    lat: str
    long:str
    words: str


@masterAgent.on_message(WeatherData)
async def receive_weather(ctx: Context, sender:str, msg:WeatherData):
    ctx.logger.info(f"Received response from {sender}:{msg.conditions}")
    ctx.logger.info(msg)
    recordedConditions = msg.conditions
    print(recordedConditions)


@masterAgent.on_message(model=Message)
async def receive_words(ctx:Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.words}")
    words = msg.words
    What3WordsFile = open("What3Words.txt", "w") 
    What3WordsFile.write(words)
    What3WordsFile.close()
    


@masterAgent.on_interval(period=30)
async def What3WordsRequest(ctx:Context):
    CoordinatesFile=open(r"location_data.txt","r")
    latitude = CoordinatesFile.readline()
    longitude = CoordinatesFile.readline()
    await ctx.send(what3WordsAgentAddress, Message(lat=latitude, long=longitude, words="None"))


def Startup():
    if __name__ == "__main__":
        masterAgent.run()



Startup()
