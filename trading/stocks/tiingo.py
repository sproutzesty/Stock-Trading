import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'token=ad9c70d5ba181c3bd1389b4ddbb6ecf6b108bf10'
}

def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/()".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()