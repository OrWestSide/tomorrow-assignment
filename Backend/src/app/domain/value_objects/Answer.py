from dataclasses import dataclass


@dataclass
class Answer:
    question_id: int = None
    answer: str = None
