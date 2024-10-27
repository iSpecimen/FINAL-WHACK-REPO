from uagents import Agent, Bureau, Context, Model
from uagents.setup import fund_agent_if_low


class Message(Model):
    timing: bool

timingAgent = Agent(
    name="message",
    port=8003,
    seed="timingRecovery",
    endpoint="http://localhost:8003/submit",
)

fund_agent_if_low(timingAgent.wallet.address())


PARKING = "agent1qtl9q7vr2xp5euvz35wy6thq98c5qlhuaj36c90lpzg4d65srlg7quvwhpl"


@timingAgent.on_interval(period=10.0)
async def send_message(ctx: Context):
    await ctx.send(PARKING, Message(timing = True))


if __name__ == "__main__":
    timingAgent.run()

if __name__ == "__main__":
    timingAgent.run()
