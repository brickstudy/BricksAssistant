import os
import openai

from src.infra.gpt.abs_gpt import AbstractApiGPT


class ChatGPT(AbstractApiGPT):
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_TOKEN"))
        self.model = "gpt-4o-mini"
        self.messages = [
            {
                "role": "system",
                "content": "너의 이름은 brickAssistant 이야. 답변은 한국어를 기본으로 해줘. "
                + "답변 마지막에 핵심 내용만 bullet form으로 요약해줘. 핵심 요약이라는 말 없이 바로 bullet form으로 요약해줘"
            }
        ]

    def request_gpt(self, msg: str, history: list = []):
        try:
            for old_msg in history:
                self.messages.append(
                    {"role": "assistant", "content": old_msg}
                )

            self.messages.append(
                {"role": "user", "content": msg}
            )
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages
            )
            return response
        # TODO : 예외 케이스 custom exception으로 수정 필요!!
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.status_code)
            print(e.response)
