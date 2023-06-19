import json
import os
import urllib.request
def lambda_handler(event, context):
    teams = "(Webhook gerado)"
    s1 = json.dumps(event)
    d2 = json.loads(s1)
    print(d2) # adicione esta linha para imprimir o valor de "d2"
    message = {'text': 'An ASG event occurred.'}
    if d2['detail']['eventName'] == 'DeleteTags':
        tags = d2['detail']['requestParameters']['tags']
        resourceId = tags[0]['resourceId'] if tags else None
        message['text'] = f"Uma tag foi deletada do ASG {resourceId} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
    elif d2['detail']['eventName'] == 'CreateOrUpdateTags':
        tags = d2['detail']['requestParameters']['tags']
        resourceId = tags[0]['resourceId'] if tags else None
        message['text'] = f"Uma tag foi adicionada ao ASG {resourceId} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
    data = json.dumps(message).encode('ascii')
    req = urllib.request.Request(teams, data)
    try:
        response = urllib.request.urlopen(req)
        response.read()
    except Exception as e:
        print(e)
