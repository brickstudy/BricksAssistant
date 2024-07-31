from src.application.entity import GPTConversationInfo


class GPTRequestService:
    def request_answer(self, client, db, info: GPTConversationInfo):
        # find history
        history = []
        if info.thread_id:
            response = db.get_item(info.thread_id)
            for r in response:
                history_q = r["question"]
                hisotry_a = r["record"]
                content = f"user: {history_q}, brickAssistant: {hisotry_a}"
                history.append(content)

        # request gpt
        response = client.request_gpt(info.question, history)
        all_answer = response.choices[0].message.content

        # split answer
        lines = all_answer.split('\n-')
        info.answer = lines[0]
        if len(lines) > 1:
            info.record = ", ".join(lines[1:])

        # insert db
        items = info.to_dict()
        db.insert_item(items)

        return info
