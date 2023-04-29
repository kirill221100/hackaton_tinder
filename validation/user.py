from pydantic import BaseModel
from typing import List


class RegistrationUser(BaseModel):
    username: str
    password: str


class EditTopics(BaseModel):
    topics: List[str]
