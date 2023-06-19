import json
import os
import urllib.request

def lambda_handler(event, context):
  teams ="(Webhook gerado)"
  s1 = json.dumps(event)
  d2 = json.loads(s1)
  print(d2) # adicione esta linha para imprimir o valor de "d2"
  message = {'text': 'Uma alteração foi realizada no S3.'}
  if d2['detail']['eventName'] == 'DeleteBucketTagging':
    message['text'] = f"Uma tag foi removida do bucket {d2['detail']['requestParameters']['bucketName']} bucket pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'PutBucketTagging':
    message['text'] = f"Uma tag foi adicionada do bucket {d2['detail']['requestParameters']['bucketName']} bucket pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'DeleteBucket':
    message['text'] = f"Um bucket de nome {d2['detail']['requestParameters']['bucketName']} foi deletado pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'CreateBucket':
    message['text'] = f"Um bucket de nome {d2['detail']['requestParameters']['bucketName']} foi criado pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."  
  data = json.dumps(message).encode('ascii')
  req = urllib.request.Request(teams, data)
  try:
    response = urllib.request.urlopen(req)
    response.read()
  except Exception as e:
    print(e)
