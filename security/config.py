import os
from dotenv import load_dotenv

load_dotenv('./.env')


class Config:
    PSQL_URL = os.environ.get('PSQL_URL')
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SECRET_KEY = os.environ.get('SECRET_KEY')
