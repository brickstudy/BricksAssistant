class ShortcutService:
    def get_shortcut(self, db):
        answer = ["Brickstudy 바로가기 링크 입니다.\n\n"]
        shortcuts = db.get_items()
        for s in shortcuts:
            answer.append(f"{s.id}. {s.name}: {s.url}\n")
        return "".join(answer)
