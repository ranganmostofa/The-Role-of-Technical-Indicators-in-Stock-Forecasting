from Signals import Signals
from collections import deque
from InventoryValuationMethods import InventoryValuationMethods as IVM


class BackTester:
    """

    """
    def __init__(self):
        pass

    def backtest(self, prices, aggregate_signals, inventory_valuation_method):
        """

        :param prices:
        :param aggregate_signals:
        :param inventory_valuation_method:
        :return:
        """
        return self.backtest_fifo(prices, aggregate_signals) if inventory_valuation_method == IVM.FIFO else \
            self.backtest_lifo(prices, aggregate_signals) if inventory_valuation_method == IVM.LIFO else \
            self.backtest_weighted(prices, aggregate_signals)

    def backtest_fifo(self, prices, aggregate_signals):
        realized_pnl = 0
        num_stocks = 0
        buy_queue = list()
        sell_queue = list()
        account_balance = 10000
        amount_invested = 0
        for index in range(len(prices)):
            if aggregate_signals[index] == Signals.BUY:
                if len(sell_queue) == 0:
                    buy_queue.append(prices[index])
                else:
                    popped_sell_price = sell_queue[0]
                    sell_queue = sell_queue[1:]
                    realized_pnl += popped_sell_price - prices[index]
                num_stocks += 1
                account_balance -= prices[index]
                amount_invested += prices[index]
            elif aggregate_signals[index] == Signals.SELL:
                if len(buy_queue) == 0:
                    sell_queue.append(prices[index])
                else:
                    popped_buy_price = buy_queue[0]
                    buy_queue = buy_queue[1:]
                    realized_pnl += prices[index] - popped_buy_price
                num_stocks -= 1
                account_balance += prices[index]
                amount_invested -= prices[index]
            else:
                continue
        unrealized_pnl = self.compute_unrealized_pnl(buy_queue, sell_queue, prices[-1])
        return amount_invested , num_stocks, realized_pnl, unrealized_pnl, realized_pnl + unrealized_pnl

    def backtest_lifo(self, prices, aggregate_signals):
        pass

    def backtest_weighted(self, prices, aggregate_signals):
        pass

    def compute_unrealized_pnl(self, net_buy_queue, net_sell_queue, final_price):
        """

        :param net_buy_queue:
        :param net_sell_queue:
        :param final_price:
        :return:
        """
        unrealized_pnl = 0
        for price in net_buy_queue:
            unrealized_pnl += final_price - price
        for price in net_sell_queue:
            unrealized_pnl += price - final_price
        return unrealized_pnl

