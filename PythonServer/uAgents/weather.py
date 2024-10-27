from uagents import Agent, Bureau, Context, Model
from uagents.setup import fund_agent_if_low

class WeatherForecastRequest(Model):
    location: str


class WeatherForecastResponse(Model):
    location: str
    temp: float
    condition: str
    humidity: float
    wind_speed: float


class WeatherData(Model):
    conditions: str

recordedConditions

agent = Agent(
    name="weather",
    endpoint="http://localhost:8000/submit",
    mailbox="917eb187-a21d-4b6a-82c7-9d6e569f89c2",
)

MASTER = ""

print(agent.address)

fund_agent_if_low(agent.wallet.address())

AI_AGENT_ADDRESS = "agent1qfvydlgcxrvga2kqjxhj3hpngegtysm2c7uk48ywdue0kgvtc2f5cwhyffv"

location = "London"

@agent.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send(AI_AGENT_ADDRESS, WeatherForecastRequest(location=location))
    ctx.logger.info(f"Sent request to weather agent: {location}")


@agent.on_message(WeatherForecastResponse)
async def handle_response(ctx: Context, sender: str, msg: WeatherForecastResponse):
    ctx.logger.info(f"Received response from {sender}:")
    ctx.logger.info(msg)
    recordedConditions = msg.condition

@agent.on_message(WeatherData)
async def send_weather(ctx: Context):
    await ctx.send(MASTER, WeatherData(conditions=recordedConditions))

"""
master data:

class WeatherData(Model):
    conditions: str

@master.on_message(WeatherData)
async def receive_weather(ctx: Context, sender:str, msg:WeatherData):
    ctx.logger.info(f"Received response from {sender}:")
    ctx.logger.info(msg)
    recordedConditions = msg.condition


"""



if __name__ == "__main__":
    agent.run()
