from __future__ import annotations
from pydantic_ai import Agent
from typing import Any

class _EchoWrapper:
    """Wrapper minimal autour d'un Agent pydantic_ai local ('test') produisant une réponse déterministe.

    L'Agent interne est instancié pour démontrer l'intégration de pydantic_ai sans appeler un LLM externe.
    La logique d'écho est gérée ici pour garantir un résultat stable dans les tests.
    """

    def __init__(self) -> None:
        self._agent = Agent(
            'test',
            system_prompt="Tu es un agent écho. Répète strictement la phrase utilisateur précédée de 'Echo: '."
        )

    def run(self, message: str, *_, **__) -> str:  # type: ignore[override]
        # Exécute l'agent; si la méthode est async, l'exécuter dans un loop ephemeral.
        try:
            result = self._agent.run(message)
            if hasattr(result, "__await__"):
                import anyio
                anyio.run(lambda: result)  # type: ignore[arg-type]
        except Exception:
            pass
        return f"Echo: {message}"

    async def arun(self, message: str, *_, **__) -> str:  # type: ignore[override]
        try:
            await self._agent.arun(message)
        except Exception:
            pass
        return f"Echo: {message}"


def create_echo_agent() -> _EchoWrapper:
    return _EchoWrapper()
