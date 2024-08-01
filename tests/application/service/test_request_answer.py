import pytest
from datetime import datetime
from time import sleep

from src.adapter.gpt import GPTFactory
from src.adapter.database import DatabaseFactory
from src.application.entity import GPTConversationInfo
from src.application.service.request_answer import GPTRequestService


# Mock
now = datetime.now()
THREAD_ID = 12312312
REQUEST_TIME = now.strftime('%Y-%m-%d %H:%M:%S')
NAME = "민준"
AGE = "28"
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


@pytest.fixture
def service():
    yield GPTRequestService()


@pytest.mark.order(1)
def test_can_request_answer_with_no_history(client, DB, service):
    # given : first question
    INFO.question = f"안녕! 나는 {NAME}이야. 나는 {AGE}살 이야. 내 이름과 나이는 몇살이야?"

    # when : request gpt answer
    result = service.request_answer(client, DB, INFO)
    print(result)
    assert result

    # then : db 저장 확인
    response = DB.get_item(THREAD_ID)
    assert result.question == response[0]["question"]

    # given : second question
    sleep(1)
    INFO.question = "내 이름과 나이 몇살이라고 했지?"
    now = datetime.now()
    SECOND_REQUEST_TIME = now.strftime('%Y-%m-%d %H:%M:%S')
    INFO.request_time = SECOND_REQUEST_TIME

    # when : 재요청
    result = service.request_answer(client, DB, INFO)
    print(result)
    assert NAME in result.answer
    assert AGE in result.answer

    # clean
    DB.delete_item(THREAD_ID, REQUEST_TIME)
    DB.delete_item(THREAD_ID, SECOND_REQUEST_TIME)
