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
                "content": "Your name is brickAssistant. Respond in Korean. "
                + "The role of assistant's message is the content of your previous conversation with me. "
                + "At the end of your response, summarize the key points in bullet form. "
                + "Provide the summary in English and indicate it as [Summary] followed by the bullet points."
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
