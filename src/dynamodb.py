import os
import boto3
from boto3.dynamodb.conditions import Key


class Dynamodb:
    def __init__(self) -> None:
        dynamodb = boto3.resource('dynamodb',
                                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                                  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                                  region_name=os.getenv("AWS_DEFAULT_REGION"))
        self.table = dynamodb.Table("brickstudy")

    def insert_item(self, item: dict):
        if item:
            self.table.put_item(Item=item)

    def get_item(self, thread_id: str):
        try:
            response = self.table.query(
                KeyConditionExpression=Key('thread_id').eq(thread_id)
                )
            return response["Items"]
        except Exception:
            return []

    def delete_item(self, thread_id: str, request_time: str):
        self.table.delete_item(Key={
            'thread_id': thread_id,
            "request_time": request_time
            })
