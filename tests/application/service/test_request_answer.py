import pytest
from datetime import datetime

from src.adapter.gpt import GPTFactory
from src.adapter.database import DatabaseFactory
from src.application.entity import GPTConversationInfo


# Mock
now = datetime.now()
THREAD_ID = 12312312
REQUEST_TIME = now.strftime('%Y-%m-%d %H:%M:%S')
NAME="민준"
AGE="28"
INFO = GPTConversationInfo(
        user_id=54231,
        user_name=NAME,
        request_time=REQUEST_TIME,
        question="",
        thread_id=THREAD_ID
    )


@pytest.fixture
def client():
    yield GPTFactory.create_client(gpt_type="chatgpt")


@pytest.fixture
def DB():
    yield DatabaseFactory.create_database_gpt("dynamodb")


@pytest.mark.order(1)
def test_can_request_answer_with_no_history(client, DB):
    # given : 유효한 요청(history X)
    INFO.question = f"안녕! 나는 {NAME}이야. 나는 {AGE}살 이야."

    # when : gpt 요청
    response = client.request_gpt(INFO.question)
    all_answer = response.choices[0].message.content

    # when : 응답 파싱
    lines = all_answer.split('\n-')
    INFO.answer = lines[0]
    if len(lines) > 1:
        INFO.record = ", ".join(lines[1:])

    # DB : 저장
    items = INFO.to_dict()
    DB.insert_item(items)

    # then : db 저장 확인
    response = DB.get_item(THREAD_ID)
    assert response

    history = []
    for r in response:
        history_q = r["question"]
        hisotry_a = r["record"]
        content = f"user: {history_q}, brickAssistant: {hisotry_a}"
        history.append(content)

    # when 재응답
    NEW_INFO = GPTConversationInfo(
        user_id=54231,
        user_name="민준",
        request_time=REQUEST_TIME,
        question="",
        thread_id=THREAD_ID
    )
    NEW_INFO.question = "내 이름이랑 나이 알려줘"
    response = client.request_gpt(NEW_INFO.question, history)
    all_answer = response.choices[0].message.content

    # then : 데이터 조회 불가 > 빈 리스트 반환
    print(all_answer)
    assert NAME in all_answer
    assert AGE in all_answer
