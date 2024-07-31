from abc import ABC, abstractmethod


class AbstractDatabaseGPT(ABC):
    @abstractmethod
    def insert_item(self, item: dict):
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
