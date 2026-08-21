"""LOADING QUESTIONS FROM JSON TO QUESTIONS TABLE"""

import json
from pathlib import Path

from sqlmodel import Session, select

from app.core.db import engine
from app.models.question import Question, QuestionType

DATA_DIR = Path(__file__).parent.parent / "data"



def load_questions() -> list[Question]:
    questions: list[Question] = []
    for json_path in sorted(DATA_DIR.glob("seed_*.json")):
        print(f" 📄Loading {json_path.name}")
        with open(json_path) as f:
            data = json.load(f)
        for q in data:
            questions.append(
                Question(
                    type=QuestionType(q["type"]),
                    year=q["year"],
                    unit=q["unit"],
                    prompt=q["prompt"],
                    choices=q.get("choices"),
                    answer=q["answer"],
                    explanation=q.get("explanation"),
                    source=q.get("source","unknown"),
                )
            )
    return questions


def seed() -> None:
    with Session(engine) as session:
        existing = session.exec(select(Question)).first()
        if existing:
            print("⚠️ Questions already exist. Skipping seed.")
            return

        questions = load_questions()
        if not questions:
            print(f"⚠️ No JSON files found in {DATA_DIR}")
            return

        for q in questions:
            session.add(q)
        session.commit()
        print(f"✅ Seeded {len(questions)} questions")


if __name__ == "__main__":
    seed()