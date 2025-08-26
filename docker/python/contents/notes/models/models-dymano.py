import boto3
import os
from uuid import uuid4

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
TABLE_NAME = os.getenv('DYNAMODB_TABLE', 'stress-test-dynamodb')

class Note:
    table = dynamodb.Table(TABLE_NAME)

    @staticmethod
    def create(title, body):
        note_id = str(uuid4())
        Note.table.put_item(
            Item={'id': note_id, 'title': title, 'body': body}
        )
        return note_id

    @staticmethod
    def get_all():
        response = Note.table.scan()
        return response.get('Items', [])

    @staticmethod
    def delete(note_id):
        Note.table.delete_item(Key={'id': note_id})