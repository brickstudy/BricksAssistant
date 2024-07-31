from dataclasses import dataclass


@dataclass
class GPTConversationInfo:
    user_id: int
    user_name: str
    request_time: str
    question: str
    thread_id: int = None
    answer: str = None
