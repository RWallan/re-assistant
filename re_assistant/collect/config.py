"""Define as configurações dos requests."""

from pathlib import Path
from typing import Type

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

HERE = Path(__file__).parent


class Headers(BaseModel):
    """Representa as informações do header do HTTP."""

    accept: str
    accept_language: str
    cache_control: str
    priority: str
    referer: str
    sec_ch_ua: str
    sec_ch_ua_mobile: str
    sec_ch_ua_platform: str
    sec_fetch_dest: str
    sec_fetch_mode: str
    sec_fetch_site: str
    sec_fetch_user: str
    sec_gpc: str
    upgrade_insecure_requests: str
    user_agent: str


class Settings(BaseSettings):
    """Define as configurações para as requisições HTTP."""

    model_config = SettingsConfigDict(toml_file=HERE / 'config.toml')
    catalog_url: str
    headers: Headers

    @classmethod
    def settings_customise_sources(  # noqa
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


settings = Settings()  # pyright: ignore
