import pytest
from datetime import datetime
from dotenv import load_dotenv
from src.adapter.database import DatabaseFactory


load_dotenv()

# Mock
THREAD_ID = "126765985734800183455"
now = datetime.now()
REQUEST_TIME = now.strftime('%Y-%m-%d %H:%M:%S')
CHANNEL_NAME = "bricksgpt-test"
NAME = "robertmin522"
USER_MSG = f"안녕 BrickAssitant. 나는 {NAME}이야"


@pytest.fixture
def DB():
    yield DatabaseFactory.create_database_gpt("dynamodb")


@pytest.mark.order(1)
def test_db_can_put_item(DB):
    # given : 유효한 thread_id, request_time
    item = {
        "thread_id": THREAD_ID,
        "request_time": REQUEST_TIME,
        "channel_name": CHANNEL_NAME,
        "user_name": NAME,
        "user_message": USER_MSG
    }

    # when : 데이터 쓰기 요청
    DB.insert_item(item=item)

    # then : 데이터 있는지 확인
    response = DB.get_item(THREAD_ID)
    assert response


@pytest.mark.order(2)
def test_db_can_get_item_with_thread_id(DB):
    # given : thread_id
    # when : 데이터 읽기 요청
    response = DB.get_item(THREAD_ID)

    # then : 데이터 확인
    item = response[0]
    assert item["thread_id"] == THREAD_ID
    assert item["channel_name"] == CHANNEL_NAME
    assert item["user_name"] == NAME
    assert item["user_message"] == USER_MSG


@pytest.mark.order(3)
def test_db_can_delete_item_with_thread_id(DB):
    # given : thread_id
    # when : 데이터 삭제 요청
    DB.delete_item(THREAD_ID, REQUEST_TIME)

    # then : 데이터 조회 불가 > 빈 리스트 반환
    response = DB.get_item(THREAD_ID)
    assert response == []


def test_db_can_get_item_with_no_thread_id(DB):
    # given : DB에 없는 thread_id 요청
    WRONG_THREAD_ID = "wrong12312311"

    # when : 데이터 쓰기 요청
    # then : 데이터 조회 불가 > 빈리스트
    response = DB.get_item(WRONG_THREAD_ID)
    assert response == []
