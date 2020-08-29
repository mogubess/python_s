from oandapyV20 import API
import configparser

print('test')

conf = configparser.ConfigParser()
conf.read('settings.ini')

account_id = conf['oanda']['account_id']
access_token = conf['oanda']['access_token']


class APIClient(object):
    def __init__(self, access_token, environment='practice'):
        self.access_token = access_token
        self.client = API(access_token=access_token, environment=environment)


testAPI = APIClient(
    '2bccf50333c7d68cb588b62e3e6d056d-7d6958d0fa930f84a112afffc569bbdc')
print(testAPI)
print(help(API))
