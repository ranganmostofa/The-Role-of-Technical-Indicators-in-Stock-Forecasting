from time import time
from FileIO import FileIO
from DataProcessing import DataProcessing
from TechnicalIndicators import TechnicalIndicators


t0 = time()

CSV_FILENAME = "S&P500 (October 19, 2007 - October 19, 2017).csv"

LONG = 200
SHORT = 50
SIGNAL = 35

field1 = "\"SPY.Open\""
field2 = "\"SPY.Close\""
data_matrix = FileIO.read_csv(CSV_FILENAME)

prices = [float(price) for price in DataProcessing.extract_prices(data_matrix, field1, field2)]

s = TechnicalIndicators.MACD.compute_aggregate_signals(prices, LONG, SHORT, SIGNAL)

print(s)

t1 = time()

print(str(t1 - t0))

