# statistics.py

class Statistics:
    def __init__(self):
        self.win_count = 0
        self.loss_count = 0
        self.trading_history = []

    def record_trade(self, result, trade):
        self.trading_history.append(trade)
        if result == 'win':
            self.win_count += 1
        elif result == 'loss':
            self.loss_count += 1

    def get_performance_metrics(self):
        total_trades = self.win_count + self.loss_count
        win_rate = (self.win_count / total_trades * 100) if total_trades > 0 else 0
        return {
            'wins': self.win_count,
            'losses': self.loss_count,
            'win_rate': win_rate,
            'total_trades': total_trades
        }

# Example usage:
# stats = Statistics()
# stats.record_trade('win', {'symbol': 'AAPL', 'amount': 10})
# print(stats.get_performance_metrics())