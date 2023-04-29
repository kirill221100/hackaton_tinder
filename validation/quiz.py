from pydantic import BaseModel
from typing import List, Optional


class AnswerOption(BaseModel):
    title: str
    is_right: bool = False


class Question(BaseModel):
    title: str
    answers: List[AnswerOption]


class QuizValidation(BaseModel):
    questions: List[Question]
