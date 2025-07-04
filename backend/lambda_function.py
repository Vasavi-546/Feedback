import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FeedbackTable')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    feedback_id = str(uuid.uuid4())

    table.put_item(Item={
        'id': feedback_id,
        'message': data['message'],
        'timestamp': datetime.now().isoformat()
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Feedback saved successfully!'})
    }

