from abc import ABC, abstractmethod


class AbstractApiGPT(ABC):
    @abstractmethod
    def request_gpt(self, msg: str, history: list = []):
        """GPT에 이전 history와 현재 메시지로 요청하는 추상화 매서드"""
        pass
