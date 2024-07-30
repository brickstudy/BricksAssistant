import os
import pytest
import boto3
from datetime import datetime
from dotenv import load_dotenv
from boto3.dynamodb.conditions import Key


load_dotenv()

# Mock
THREAD_ID = "126765985734800183455"
now = datetime.now()
REQUEST_TIME = now.strftime('%Y-%m-%d %H:%M:%S')
CHANNEL_NAME = "bricksgpt-test"
NAME = "robertmin522"
USER_MSG = f"안녕 BrickAssitant. 나는 {NAME}이야"


@pytest.fixture
def table():
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                              aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                              region_name=os.getenv("AWS_DEFAULT_REGION"))

    yield dynamodb.Table("brickstudy")


@pytest.mark.order(1)
def test_db_can_put_item(table):
    # given : 유효한 thread_id, request_time
    item = {
        "thread_id": THREAD_ID,
        "request_time": REQUEST_TIME,
        "channel_name": CHANNEL_NAME,
        "user_name": NAME,
        "user_message": USER_MSG
    }

    # when : 데이터 쓰기 요청
    table.put_item(Item=item)

    # then : 데이터 있는지 확인
    response = table.query(
        KeyConditionExpression=Key('thread_id').eq(THREAD_ID)
    )
    assert response


@pytest.mark.order(2)
def test_db_can_get_item_with_thread_id(table):
    # given : thread_id
    # when : 데이터 읽기 요청
    response = table.query(
        KeyConditionExpression=Key('thread_id').eq(THREAD_ID)
    )

    # then : 데이터 확인
    item = response["Items"][0]
    assert item["thread_id"] == THREAD_ID
    assert item["channel_name"] == CHANNEL_NAME
    assert item["user_name"] == NAME
    assert item["user_message"] == USER_MSG


@pytest.mark.order(3)
def test_db_can_delete_item_with_thread_id(table):
    # given : thread_id
    # when : 데이터 삭제 요청
    table.delete_item(
        Key={
            'thread_id': THREAD_ID,
            "request_time": REQUEST_TIME
        }
    )

    # then : 데이터 조회 불가 > 빈 리스트 반환
    response = table.query(
            KeyConditionExpression=Key('thread_id').eq(THREAD_ID)
        )
    items = response["Items"]
    assert not items


def test_db_can_get_item_with_no_thread_id():
    # given : DB에 없는 thread_id 요청
    WRONG_THREAD_ID = "wrong12312311"

    # when : 데이터 쓰기 요청
    # then : 데이터 조회 불가
    with pytest.raises(AttributeError):
        table.query(
            KeyConditionExpression=Key('thread_id').eq(WRONG_THREAD_ID)
        )
