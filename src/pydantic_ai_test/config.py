from __future__ import annotations
from pydantic_settings import BaseSettings
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import AnyUrl

class AppSettings(BaseSettings):
    api_base_url: AnyUrl = "https://api.example.com"
    support_phone: PhoneNumber | None = None
    debug: bool = False

    model_config = {
        "env_prefix": "APP_",
        "case_sensitive": False,
    }
