from fastapi import Depends
from fastapi.security import HTTPBearer
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()

def verify_token(credentials=Depends(security)):
    token = credentials.credentials

    payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def create_acess_token(data: dict):
    to_encoda = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encoda.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encoda,SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
