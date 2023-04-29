from pydantic import BaseModel
from typing import List, Optional


class ProfileValidation(BaseModel):
    text: str
    topics: List


class ProfileEdit(BaseModel):
    text: Optional[str]
    topics: Optional[List[str]]

