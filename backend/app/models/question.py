from datetime import datetime
from enum import Enum
from typing import Optional 

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel



class QuestionType(str, Enum):
    MCQ = 'mcq'
    FRQ = 'frq'



class Question(SQLModel, table=True):
    """ A single AP CSA practice question (MCQ or FRQ)."""
    __tablename__ = "questions"

    id: Optional[int] = Field(default=None, primary_key=True)
    type: QuestionType = Field(index=True)
    year: int = Field(index=True)
    unit: int = Field(index=True)
    prompt: str

    # MCQ: list of {key: "A", text: "..."} dicts; FRQ: null
    choices: Optional[list[dict]] = Field(default=None, sa_column=Column(JSON))


    # MCQ: correct key (e.g. "A"); FRQ: solution code (Java)
    answer: str
    explanation: Optional[str] = None


    # FRQ-only fields
    starter_code: Optional[str] = None
    public_tests: Optional[list[dict]] = Field(default=None, sa_column=Column(JSON))
    hidden_tests: Optional[list[dict]] = Field(default=None, sa_column=Column(JSON))


    # Source metadata
    source: str = Field(default="college_board", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


    


