import  unittest
from input.inp import inpu
from mai import mai
from requests import Request, Session
from collections import namedtuple
class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session=Session()
        cls.session.headers.update({

            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })
        AuthenticationCredentials = namedtuple('AuthenticationCredentials',
                                               'auth_id auth_token')

        def fetch_credentials(auth_id, auth_token):
            """Fetches the right credentials either from params or from environment"""

            return AuthenticationCredentials(auth_id=auth_id, auth_token=auth_token)
        cls.session.auth = fetch_credentials(inpu.Authid, inpu.token)


    def test_case1(self):
        url = "https://api.plivo.com/v1/Account/"+inpu.Authid+"/"
        fetchMethods=mai(url,self.session)
        r=fetchMethods.getMethod("")
        assert r.status_code == 200
        initial = r.json()['cash_credits']
        r=fetchMethods.getMethod(inpu.numberURL)
        assert r.status_code==200
        num1 = (r.json()['objects'][0]['number'])
        num2 = (r.json()['objects'][1]['number'])
        data = "{\"src\" : \""+num1+"\",\"dst\" : [\""+num2+"\"],\"text\" :\"hello\"}"
        r=fetchMethods.postMethod(inpu.sendmessageurl,data)
        assert r.status_code == 202
        uuid = r.json()['message_uuid'][0]
        r=fetchMethods.getMethod(inpu.sendmessageurl+"/"+uuid+"/")
        assert r.status_code==200
        outboundrate = r.json()['total_rate']
        data = {'country_iso': inpu.countryISO}
        r=fetchMethods.getMethodParam(inpu.pricin,data)
        assert r.status_code==200
        rate = (r.json()['message']['outbound']['rate'])
        assert rate==outboundrate
        fetchMethods=mai(url,self.session)
        r=fetchMethods.getMethod("")
        assert r.status_code == 200
        final = r.json()['cash_credits']
        assert final<initial
        print('Complete')






if __name__ == '__main__':
    unittest.main()
