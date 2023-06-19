import json
import os
import urllib.request

def lambda_handler(event, context):
  teams ="(webhook gerado)"
  s1 = json.dumps(event)
  d2 = json.loads(s1)
  print(d2) # adicione esta linha para imprimir o valor de "d2"
  message = {'text': 'An RDS event occurred.'}
  if d2['detail']['eventName'] == 'RemoveTagsFromResouce':
    message['text'] = f"A tag foi removida do banco {d2['detail']['requestParameters']['resourceName']} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'AddTagsToResource':
    message['text'] = f"A tag foi adicionada no banco {d2['detail']['requestParameters']['resourceName']} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  data = json.dumps(message).encode('ascii')
  req = urllib.request.Request(teams, data)
  try:
    response = urllib.request.urlopen(req)
    response.read()
  except Exception as e:
    print(e)
