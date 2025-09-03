import os
from pydantic_ai_test import AppSettings


def test_settings_env(monkeypatch):
    monkeypatch.setenv("APP_API_BASE_URL", "https://example.org")
    monkeypatch.setenv("APP_DEBUG", "true")
    s = AppSettings()
    assert str(s.api_base_url).rstrip('/') == "https://example.org"
    assert s.debug is True
