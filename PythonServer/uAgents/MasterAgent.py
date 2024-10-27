#MASTER UAGENT#

from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Protocol, Model
import random
from uagents import Field

import sys

import CarParks
import Weather

CarParkAgentAddress="agent1q2a45mxzld7ffe484ejup3g4mqk83x4hf8qhhl7ratzyh5x3s0kuk6vwqrn"
what3WordsAgentAddress="agent1qfc5uu3mseyrnwwnw675pwve685ysduk36zhtaasw2ad5kar8x67g6fgsdv"

class CarParksMessage(Model):
    message:str

class what3WordsMessage(Model):
    lat: str
    long:str
    words: str

masterAgent = Agent(
    name="masterAgent",
    port=8000,
    seed="MASTER AGENT",
    endpoint=["http://localhost:8000/submit"],
)

@masterAgent.on_event("startup")
async def GetWeather(ctx:Context):
    await ctx.send(CarParkAgentAddress, CarParksMessage(message=True))

def Startup():
    if __name__ == "__main__":
        masterAgent.run()




