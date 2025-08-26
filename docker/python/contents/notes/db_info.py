import boto3
import logging
from django.conf import settings
from pymongo import MongoClient
import urllib.parse

logger = logging.getLogger(__name__)

def get_db_info():
    # DynamoDB 判定
    try:
        from .models import Note
        notes = Note.get_all()
        if isinstance(notes, list):  # 結果がリストなら DynamoDB
            client = boto3.client('dynamodb', region_name='ap-northeast-1')
            response = client.describe_table(TableName=Note.table.name)
            return {
                'engine': 'DynamoDB',
                'cluster': response['Table']['TableName']
            }
    except Exception as e:
        pass

    # DocumentDB 判定
    try:
        db_config = settings.MONGODB_DATABASES['default']
        username = urllib.parse.quote_plus(db_config['username'])
        password = urllib.parse.quote_plus(db_config['password'])
        host = db_config['host']

        uri = (
            f"mongodb://{username}:{password}@{host}:27017/"
            "?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false"
        )

        client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        server_info = client.server_info()

        return {
            'engine': 'DocumentDB',
            'cluster': host
        }
    except Exception as e:
        pass

    return {
        'engine': '不明',
        'cluster': '不明'
    }
