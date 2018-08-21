import dmarketpy as apimodule
api = apimodule.API()
api.load_key("api_key.key")

def games():
    #For urlpaths see: https://docs.dmarket.com/api/trading/swagger/ui/#!/
    urlpath = "/game/v1/games"
    #No authentication key required, so we use public_query.
    print(api.public_query(urlpath=urlpath))


def user_balance():
    urlpath="/account/v1/user/balance"
    #authentication key required, so we use private_query.
    #this is a GET request so we take "GET" as a type
    print(api.private_query(urlpath=urlpath,type="GET"))

def accounting_offers():
    payload = {"DateEnd": 1,
                "DateStart": 3}
    urlpath="trading/v1/report/accounting/offers"
    # authentication key required, so we use private_query.
    # this is a POST request so we take "POST" as a type
    # our body request goes straight into json
    print(api.private_query(urlpath=urlpath,type="POST",json=payload))


print("\n Games \n")
games()
print("\n User Balance \n")
user_balance()
print("\n Accounting Offers \n")
accounting_offers()

