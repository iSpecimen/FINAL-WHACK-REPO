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


PARKING = "agent1q2a45mxzld7ffe484ejup3g4mqk83x4hf8qhhl7ratzyh5x3s0kuk6vwqrn"


@timingAgent.on_interval(period=10.0)
async def send_message(ctx: Context):
    await ctx.send(PARKING, Message(timing = True))


if __name__ == "__main__":
    timingAgent.run()
