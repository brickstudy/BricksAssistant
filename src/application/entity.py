from dataclasses import dataclass, fields


@dataclass
class GPTConversationInfo:
    user_id: int
    user_name: str
    request_time: str
    question: str
    thread_id: int = None
    answer: str = None
    record: str = ""

    def to_dict(self) -> dict:
        """dataclass 인스턴스를 딕셔너리로 변환"""
        return {field.name: getattr(self, field.name) for field in fields(self)}
