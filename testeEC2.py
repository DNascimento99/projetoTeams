import json
import os
import urllib.request

def lambda_handler(event, context):
  teams = ("Webhook Gerado")
  s1 = json.dumps(event)
  d2 = json.loads(s1)
  print(d2) # adicione esta linha para imprimir o valor de "d2"
  message = {'text': 'Uma alteração foi realizada no EC2.'}
  if d2['detail']['eventName'] == 'RunInstances':
    items = d2['detail']['responseElements']['instancesSet']['items']
    instanceId = items[0]['instanceId'] if items else None
    if d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName'] != 'AWSServiceRoleForAutoScaling':
      message['text'] = f"A instância EC2 {instanceId} foi criada, pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['principalId']}."
    else:
      message['text'] = ''
  if d2['detail']['eventName'] == 'StartInstances':
    message['text'] = f"A instância EC2 {d2['detail']['requestParameters']['instancesSet']['items']} foi startada, pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['principalId']}."
  if d2['detail']['eventName'] == 'StopInstances':
    message['text'] = f"A instância EC2 {d2['detail']['requestParameters']['instancesSet']['items']} foi stopada, pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['principalId']}."
  if d2['detail']['eventName'] == 'TerminateInstances':
    items2 = d2['detail']['requestParameters']['instancesSet']['items']
    instanceId2 = items2[0]['instanceId'] if items2 else None 
    if d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['userName'] != 'AWSServiceRoleForAutoScaling':
      message['text'] = f"A instância EC2 {instanceId2} foi terminada, pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['principalId']}."
    else:
      message['text'] = ''
  if d2['detail']['eventName'] == 'DeleteTags':
    message['text'] = f"Uma tag foi removida no EC2 {d2['detail']['requestParameters']['resourcesSet']['items']} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['principalId']}."
  if d2['detail']['eventName'] == 'CreateTags':
    message['text'] = f"Uma tag foi adicionada no EC2 {d2['detail']['requestParameters']['resourcesSet']['items']} pelo usuário {d2['detail']['userIdentity']['sessionContext']['sessionIssuer']['principalId']}."
  data = json.dumps(message).encode('ascii')
  req = urllib.request.Request(teams, data)
  try:
    response = urllib.request.urlopen(req)
    response.read()
  except Exception as e:
    print(e)
