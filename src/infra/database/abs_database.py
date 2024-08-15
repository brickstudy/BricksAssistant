from abc import ABC, abstractmethod
from src.application.entity import GPTConversationInfo


class AbstractDatabaseGPT(ABC):
    @abstractmethod
    def insert_item(self, item: GPTConversationInfo):
        """데이터베이스에 GPT 요청 응답 데이터 삽입하는 추상화 메서드"""
        pass

    @abstractmethod
    def get_item(self, thread_id: str):
        """데이터베이스에 특정 thread_id 기준 응답을 가져오는 추상화 매서드"""
        pass

    @abstractmethod
    def delete_item(self, thread_id: str, request_time: str):
        """데이터베이스에 특정 thread_id 기준 응답을 삭제하는 추상화 매서드"""
        pass


class AbstractDatabaseBrickas(ABC):
    @abstractmethod
    def get_items(self):
        """데이터베이스에서 전체 바로가기 정보 가져오는 메서드"""
        pass
