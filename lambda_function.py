import json, boto3, time, uuid, urllib.request, os

dynamo = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamo.Table('ChatHistory')

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    message = body.get('message', '')
    session_id = body.get('session_id', str(uuid.uuid4()))

    api_key = os.environ['ANTHROPIC_API_KEY']

    req = urllib.request.Request(
        'https://api.anthropic.com/v1/messages',
        data=json.dumps({
            "model": "claude-haiku-4-5",
            "max_tokens": 512,
            "messages": [{"role": "user", "content": message}]
        }).encode(),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        method='POST'
    )
    response = urllib.request.urlopen(req)
    reply = json.loads(response.read())
    reply_text = reply['content'][0]['text']

    ts = int(time.time() * 1000)
    table.put_item(Item={'session_id':session_id,'timestamp':ts,'role':'user','message':message})
    table.put_item(Item={'session_id':session_id,'timestamp':ts+1,'role':'assistant','message':reply_text})

    return {
        'statusCode': 200,
        'headers': {'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        'body': json.dumps({'reply': reply_text, 'session_id': session_id})
    }
