from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Py Route"
    VERSION: str = "0.1.0"

    ADMIN_EMAIL: str = "jeanmarinho529@gmail.com"

    MAX_POINTS: int = 10


settings = Settings()
