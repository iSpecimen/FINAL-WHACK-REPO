from uagents import Agent, Bureau, Context, Model
from uagents.setup import fund_agent_if_low

class Message(Model):
    timing: bool


timingAgent = Agent(
    name="message",
    port=8003,
    seed="timingRecovery",
    endpoint=["http://127.0.0.1:8003/submit"],
)

fund_agent_if_low(timingAgent.wallet.address())

MASTER = ""
PARKING = ""


@timingAgent.on_interval(period=72000.0)
async def send_message(ctx: Context):
    await ctx.send(PARKING, Message(message = True))


@coordinates.on_message(model=Message)
async def coordinates_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.timing}")


if __name__ == "__main__":
    timingAgent.run()
