import requests

class PocketOptionsAPI:
    def __init__(self, account_id, api_key):
        self.account_id = account_id
        self.api_key = api_key
        self.base_url = 'https://api.pocketoptions.com/'

    def get_balance(self):
        url = f'{self.base_url}v1/account/balance'
        headers = { 'Authorization': f'Bearer {self.api_key}' }
        response = requests.get(url, headers=headers)
        return response.json()

    def place_trade(self, amount, direction):
        url = f'{self.base_url}v1/trade'
        headers = { 'Authorization': f'Bearer {self.api_key}' }
        trade_data = { 'amount': amount, 'direction': direction }
        response = requests.post(url, json=trade_data, headers=headers)
        return response.json()

# Example usage:
# pocket_options = PocketOptionsAPI(account_id='your_account_id', api_key='your_api_key')
# balance = pocket_options.get_balance()
# print(balance)
# trade_response = pocket_options.place_trade(amount=10, direction='call')
# print(trade_response)