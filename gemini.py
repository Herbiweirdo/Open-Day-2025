
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    openai,
    noise_cancellation,
)

load_dotenv()


session = AgentSession(
    llm=google.beta.realtime.RealtimeModel(
        model="gemini-2.0-flash-exp",
        voice="Puck",
        temperature=0.8,
        instructions="You are a helpful assistant",
    ),
)