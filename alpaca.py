import alpaca_trade_api as tradeapi
import json

paper_apikeys = json.loads(open("apikeys.json").read())['alpaca_paper']


BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = paper_apikeys['public']
ALPACA_SECRET_KEY = paper_apikeys['private']


# Instantiate REST API Connection
api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v2')

btcusd = api.get_asset('BTC/USD')
print (btcusd)

print(api.get_bars("BTC/USD", tradeapi.TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df)

account = api.get_account()
print(account)


