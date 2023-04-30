from pydantic import BaseModel
from typing import List, Optional


class ProfileValidation(BaseModel):
    name: str
    text: str
    topics: List


class ProfileEdit(BaseModel):
    text: Optional[str]
    topics: Optional[List[str]]
