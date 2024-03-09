from pydantic import BaseSettings


class Settings(BaseSettings):

    server_host: str
    server_port: int
    
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_pass: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf8',
)
