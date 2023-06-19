import json
import os
import urllib.request

def lambda_handler(event, context):
  teams ="(Webhook gerado)"
  s1 = json.dumps(event)
  d2 = json.loads(s1)
  print(d2) # adicione esta linha para imprimir o valor de "d2"
  message = {'text': 'An IAM event occurred.'}
  if d2['detail']['eventName'] == 'CreateUser':
    message['text'] = f"Um usuario de nome {d2['detail']['requestParameters']['userName']} foi criado pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'DeleteUser':
    message['text'] = f"Um usuario de nome {d2['detail']['requestParameters']['userName']} foi deletado pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'CreateRole':
    message['text'] = f"Uma role de nome {d2['detail']['requestParameters']['roleName']} foi criado pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'DeleteRole':
    message['text'] = f"Uma role de nome {d2['detail']['requestParameters']['roleName']} foi deletado pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'DetachRolePolicy':
    message['text'] = f"Uma policy de Arn {d2['detail']['requestParameters']['policyArn']} foi deletado da role {d2['detail']['requestParameters']['roleName']} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'AttachRolePolicy':
    message['text'] = f"Uma policy de Arn {d2['detail']['requestParameters']['policyArn']} foi adicionado a role {d2['detail']['requestParameters']['roleName']} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'CreatePolicy':
    message['text'] = f"Uma policy de nome {d2['detail']['requestParameters']['policyName']} foi criado pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  if d2['detail']['eventName'] == 'DeletePolicy':
    message['text'] = f"Uma policy de Arn {d2['detail']['requestParameters']['policyArn']} foi excluída pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName']}."
  data = json.dumps(message).encode('ascii')
  req = urllib.request.Request(teams, data)
  try:
    response = urllib.request.urlopen(req)
    response.read()
  except Exception as e:
    print(e)
