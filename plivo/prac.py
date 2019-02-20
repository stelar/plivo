import requests
from requests import Request, Session
import  plivo
from collections import namedtuple
AuthenticationCredentials = namedtuple('AuthenticationCredentials',
                                       'auth_id auth_token')

def fetch_credentials(auth_id, auth_token):
    """Fetches the right credentials either from params or from environment"""
    print(AuthenticationCredentials(auth_id=auth_id, auth_token=auth_token))
    return AuthenticationCredentials(auth_id=auth_id, auth_token=auth_token)
headers={}
headers['Content-Type']='application/json'
session = Session()
session.headers.update({

            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })

session.auth = fetch_credentials('MAODUZYTQ0Y2FMYJBLOW', 'ODgyYmQxYTQ2N2FkNDFiZTNhZWY4MDAwYWY4NzY0')

r=session.get(url='https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/')
print(r.status_code)
initial=r.json()['cash_credits']
#
r=session.get(url='https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Number/')
num1 = (r.json()['objects'][0]['number'])
num2 = (r.json()['objects'][1]['number'])
print(r.status_code)
print(num1,num2)
data="{\"src\" : \"14158408589\",\"dst\" : [\"14158408583\"],\"text\" :\"heelo\"}"
sendmessageurl='https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Message/'
r=session.post(url=sendmessageurl,data=data)
print(r.status_code)
uuid=r.json()['message_uuid'][0]
print(uuid)
r=session.get(url="https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Message/"+uuid+"/")
print(r.status_code)
outboundrate=r.json()['total_rate']
data={'country_iso':'US'}
r=session.get(url="https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Pricing/",params=data)
print(r.status_code)
rate=(r.json()['message']['outbound']['rate'])
if rate==outboundrate:
    print('Rate is equal')


r=session.get(url='https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/')
print(r.status_code)
final=r.json()['cash_credits']
if final < initial:
    print ("deduction is correct")
