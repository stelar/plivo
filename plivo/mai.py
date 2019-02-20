import requests as r
from input.inp import inpu
from collections import namedtuple
class mai:
    AuthenticationCredentials = namedtuple('AuthenticationCredentials',
                                           'auth_id auth_token')
    def __init__(self,url,session):
        self.url=url
        self.session=session
    def getMethod(self,target):
        finUrl=self.url+target
        req=self.session.get(finUrl)
        return req

    def getMethodParam(self,target,param):
        finUrl=self.url+target
        req=self.session.get(finUrl,params=param)
        return req

    def postMethod(self,target,data):
        finUrl=self.url+target
        req = self.session.post(url=finUrl, data=data)
        return req


