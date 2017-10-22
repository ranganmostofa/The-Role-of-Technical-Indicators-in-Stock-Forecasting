from time import time
from FileIO import FileIO
from BackTester import BackTester
from DataProcessing import DataProcessing
from TechnicalIndicators import TechnicalIndicators
from InventoryValuationMethods import InventoryValuationMethods as IVM

t0 = time()

# CSV_FILENAME = "S&P500 (October 19, 2007 - October 18, 2017).csv"
CSV_FILENAME = "S&P500 (October 21, 1996 - October 18, 2017).csv"

# CSV_FILENAME = "Russell2000 (May 26, 2000 - October 18, 2017).csv"
# (100519.72166326032, 1329, 53854.414445099996, 44337.94920763997, 98192.36365273996)

# CSV_FILENAME = "NASDAQ (March 10, 1999 - October 18, 2017).csv"
# (106053.76809122023, 1459, 45761.909853290046, 65371.06351448993, 111132.97336777998)

LONG = 26
SHORT = 12
SIGNAL = 9

INVENTORY_VALUATION_METHOD = IVM.FIFO

# field1 = "SPY.Open"
# field2 = "SPY.Close"
field3 = "SPY.Adjusted"
data_matrix = FileIO.read_csv(CSV_FILENAME)

prices = [float(price) for price in DataProcessing.extract_prices(data_matrix, field3)]

s = TechnicalIndicators.MACD.compute_aggregate_signals(prices, LONG, SHORT, SIGNAL)

print(s)

bt = BackTester()

investment, position, realized_pnl, unrealized_pnl, pnl = \
    bt.backtest(prices[len(prices) - len(s):], s, INVENTORY_VALUATION_METHOD)

print(investment)
print(realized_pnl, unrealized_pnl, pnl)
print(pnl / investment * 100, "\n")

t1 = time()

print("Time Taken:", str(t1 - t0), "s")

