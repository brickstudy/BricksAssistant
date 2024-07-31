from src.infra.gpt.chatgpt import ChatGPT


class GPTFactory:
    @staticmethod
    def create_client(gpt_type: str = "chatgpt"):
        if gpt_type == "chatgpt":
            return ChatGPT()
