from typing import List, Optional
#from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
import os

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
    endpoint="http://localhost:8000/submit",
    mailbox="dfa8ec8c-a89a-4f87-953e-74b0e9a5b5fd",
    )

#fund_agent_if_low(agent.wallet.address())

AI_AGENT_ADDRESS = "agent1qwrl7t9uevlax09tsvf2lef6ehttsx6d29jklqjd44yks5zy0taq59d5fha"

latitude = 35.7174747
longitude = 139.7941792
radius = 100
max_results = 5
      

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

"""
add to master:
class CParkCoords(Model):
    latitude: float
    longitude: float

@mater.on_message(model=CParkCords)
async def carParks_message_handler(ctx: Context, sender: str, msg: CParkCoords):
    ctx.logger.info(f"Received message from {sender}: {msg.latitude}, {msg.longitude}")
    latitude = msg.latitude
    longitude = msg.longitude
"""

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
