import json
import datetime


def handler(event, context):
    data = {
        'output': 'Cry in the Dojo, laugh on the Battlefield',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
