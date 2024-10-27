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



agent = Agent(
    name="weather",
    endpoint="http://localhost:8004/submit",
    mailbox="5216c682-3c11-40ec-86c6-1248d2f84717",
)

MASTER = "agent1qw49f56dhvu5fmat3hqfngn46t9drnjswwsr3sy37l50nqhdy6wzwllpyaj"

print(agent.address)

fund_agent_if_low(agent.wallet.address())

AI_AGENT_ADDRESS = "agent1qfvydlgcxrvga2kqjxhj3hpngegtysm2c7uk48ywdue0kgvtc2f5cwhyffv"

CityFile=open("cityFile.txt", "r")
location = CityFile.read()

@agent.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send(AI_AGENT_ADDRESS, WeatherForecastRequest(location=location))
    ctx.logger.info(f"Sent request to weather agent: {location}")


@agent.on_message(WeatherForecastResponse)
async def handle_response(ctx: Context, sender: str, msg: WeatherForecastResponse):
    ctx.logger.info(f"Received response from {sender}:{msg.condition}")
    ctx.logger.info(msg)
    recordedConditions = msg.condition

    @agent.on_message(WeatherData)
    async def send_weather(ctx: Context):
        await ctx.send(MASTER, WeatherData(conditions=recordedConditions))




if __name__ == "__main__":
    agent.run()