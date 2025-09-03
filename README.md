# pydantic_ai_test

Projet minimal Python ciblant 3.13 (exécuté ici sous 3.12 si 3.13 indisponible) avec Pydantic et pydantic-ai.

## Installation

Créer un environnement virtuel (essayez d'abord 3.13, sinon 3.12) :

```bash
python3.13 -m venv .venv 2>/dev/null || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
```

## Tests

```bash
pytest
```

## Exemple rapide

```python
from pydantic_ai_test import User
print(User(id=1, email="a@example.com", name="Alice"))
```

### Exemple pydantic-ai

```python
from pydantic_ai_test import create_echo_agent
agent = create_echo_agent()
print(agent.run("Salut"))
```

## Qualité

```bash
ruff check .
mypy
```

## Notes

Mettre à jour `requires-python` à `>=3.13` quand l'environnement fournit la version.