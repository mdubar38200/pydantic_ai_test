import anyio
from pydantic_ai_test import create_echo_agent


def test_echo_agent():
    agent = create_echo_agent()
    # Selon l'impl interne, on utilise run ou arun; ici assumons run synchrone disponible
    reply = agent.run("Bonjour")
    assert reply == "Echo: Bonjour"


def test_echo_agent_async():
    agent = create_echo_agent()
    async def _call():
        return await agent.arun("Test Async")
    out = anyio.run(_call)
    assert out == "Echo: Test Async"
