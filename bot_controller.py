import time

class BotController:
    def __init__(self):
        self.is_active = False
        self.is_demo = True
        self.trade_history = []
        self.active_trades = []
        self.wins = 0
        self.losses = 0

    def toggle(self):
        self.is_active = not self.is_active
        print(f'Bot is now {'on' if self.is_active else 'off'}')

    def switch_account(self):
        self.is_demo = not self.is_demo
        account_type = 'demo' if self.is_demo else 'real'
        print(f'Switched to {account_type} account')

    def start_trade(self, trade):
        if not self.is_active:
            print('Cannot start trade: Bot is off')
            return
        self.active_trades.append(trade)
        print(f'Started trade: {trade}')

    def end_trade(self, trade, result):
        if trade in self.active_trades:
            self.active_trades.remove(trade)
            self.trade_history.append((trade, result))
            if result == 'win':
                self.wins += 1
            else:
                self.losses += 1
            print(f'Ended trade: {trade}, Result: {result}')
        else:
            print('Trade not found in active trades')

    def get_win_loss_ratio(self):
        if self.wins + self.losses == 0:
            return 'N/A'
        return self.wins / (self.wins + self.losses)

    def get_trade_history(self):
        return self.trade_history

    def get_active_trades(self):
        return self.active_trades

if __name__ == '__main__':
    controller = BotController()
    controller.toggle()  # Turn on the bot
    controller.switch_account()  # Switch to real account
    controller.start_trade('Trade 1')  # Start a trade
    time.sleep(2)  # Simulate time passing
    controller.end_trade('Trade 1', 'win')  # End the trade with a win
    print(f'Win/Loss Ratio: {controller.get_win_loss_ratio()}')
    print(f'Trade History: {controller.get_trade_history()}')