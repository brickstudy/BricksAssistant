from src.infra.gpt.chatgpt import ChatGPT


class GPTFactory:
    @staticmethod
    def create_client(gpt_type: str = "chatgpt"):
        if gpt_type == "chatgpt":
            return ChatGPT()
        else:
            raise ValueError(f"Unknown gpt type: {gpt_type}")
