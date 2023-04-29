from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from security.config import Config


def create_token(data: dict):
    exp = datetime.now() + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({'exp': exp})
    return jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)


def verify_token(token: str):
    try:
        user_data = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        if user_data:
            return user_data
        raise HTTPException(status_code=400, detail='Invalid token')
    except JWTError:
        raise HTTPException(status_code=400, detail='Invalid token')
