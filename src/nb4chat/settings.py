from dotenv import find_dotenv
from pydantic import AnyHttpUrl, Field, IPvAnyAddress
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_ignore_empty=True,
        extra="ignore",
    )

    # garage
    endpoint_url: AnyHttpUrl | str = "http://localhost:3900"
    key_id: str
    secret_key: str

    # uvicorn
    host: IPvAnyAddress | str = Field(default="0.0.0.0", description="The host address to bind to")
    port: int = Field(default=8000, ge=1, le=65535)
    reload: bool = False
    workers: int = Field(default=1, ge=1)
    allowed_origins: list[str] | None = Field(default_factory=list)


settings = Settings()  # type: ignore


def main():
    from rich.pretty import pprint

    pprint(settings)


if __name__ == "__main__":
    main()
