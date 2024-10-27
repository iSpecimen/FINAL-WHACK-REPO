from typing import List, Optional
#from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
import os

os.system("timingAgent.py")
environment = os.getenv("4c0b34056f20409d973dc88b884693c7")

class GeoParkingRequest(Model):
    latitude: float
    longitude: float
    radius_in_meters: int
    max_results: int
    

class CarPark(Model):
    name: Optional[str]
    address: Optional[str]
    latitude: float
    longitude: float

class CParkCoords(Model):
    latitude: float
    longitude: float


class GeoParkingResponse(Model):
    carparks: List[CarPark]
    
class Message(Model):
    timing: bool

MASTER = "agent1qw49f56dhvu5fmat3hqfngn46t9drnjswwsr3sy37l50nqhdy6wzwllpyaj"


carpark = Agent(
    name="user",
    endpoint="http://localhost:8002/submit",
    mailbox="fe9eb1b9-475d-43d4-8f87-34831ac8bfcc",
    )

#fund_agent_if_low(agent.wallet.address())

AI_AGENT_ADDRESS = "agent1qwrl7t9uevlax09tsvf2lef6ehttsx6d29jklqjd44yks5zy0taq59d5fha"

CoordinatesFile=open("location_data.txt","r")

latitude = CoordinatesFile.readline()
longitude = CoordinatesFile.readline()
radius = 100
max_results = 1
print(latitude)
print(longitude)

CoordinatesFile.close()
      

@carpark.on_message(model=Message)
async def send_message(ctx: Context, sender: bool, msg: Message):
    await ctx.send(
        AI_AGENT_ADDRESS,
        GeoParkingRequest(
            latitude=latitude,
            longitude=longitude,
            radius_in_meters=radius,
            max_results=max_results,
        ),
    )



@carpark.on_message(GeoParkingResponse)
async def handle_response(ctx: Context, sender: str, msg: GeoParkingResponse):
    ctx.logger.info(f"Received response from {sender}:")
    ctx.logger.info(msg.carparks)
    for i in msg.carparks:
        count = 0
        for j in i:
            if count == 0:
                CParklat = j
                #print(CParklat)
            elif count == 1:
                CParklong = j
                #print(CParklong)
            count += 1

        @carpark.on_message(model=CParkCoords)
        async def send_message(ctx: Context):
            await ctx.send(MASTER, CParkCoords(latitude = CParklat, longitude = CParklong))


if __name__ == "__main__":
    carpark.run()