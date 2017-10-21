from Signals import Signals
from WeightFunctions import WeightFunctions


class TechnicalIndicators:
    """

    """
    class MovingAverages:
        """

        """
        @staticmethod
        def compute_simple_average(values):
            """

            :param values:
            :return:
            """
            return sum(values) / float(len(values))

        @staticmethod
        def compute_weighted_average(values, weight_function):
            """

            :param values:
            :param weight_function:
            :return:
            """
            return sum([weight_function(value) / float(sum(weight_function(*values))) for value in values])

        @staticmethod
        def compute_simple_moving_average(values, window_length):
            """

            :param values:
            :param window_length:
            :return:
            """
            return [TechnicalIndicators.MovingAverages.compute_simple_average(values[start_index: start_index +
                            window_length]) for start_index in range(len(values) - window_length + 1)]

        @staticmethod
        def compute_weighted_moving_average(values, window_length, weight_function):
            """

            :param values:
            :param window_length:
            :param weight_function:
            :return:
            """
            return [TechnicalIndicators.MovingAverages.compute_weighted_average(values[start_index: start_index +
                            window_length], weight_function) for start_index in range(len(values) - window_length + 1)]

    class MACD:
        """

        """
        @staticmethod
        def compute_aggregate_signals(prices, long, short, signal):
            """

            :param prices:
            :param long:
            :param short:
            :param signal:
            :return:
            """
            return [Signals.to_signal(sum([signal_component.value for signal_component in signals_vector]))
                    for signals_vector in TechnicalIndicators.MACD.compute_separate_signals(prices, long, short, signal)]

        @staticmethod
        def compute_separate_signals(prices, long, short, signal):
            """

            :param prices:
            :param long:
            :param short:
            :param signal:
            :return:
            """
            macd = TechnicalIndicators.MACD.compute_macd(prices, long, short)
            long_ma = TechnicalIndicators.MACD.compute_long_ma(prices, long)
            short_ma = TechnicalIndicators.MACD.compute_short_ma(prices[long - short:], short)
            signal_ma = TechnicalIndicators.MACD.compute_signal_ma(prices[long - signal:], signal)

            print(long_ma)
            print(short_ma)
            print(signal_ma)
            print(macd)

            return zip(TechnicalIndicators.MACD.determine_crossover_signal(macd, signal_ma),
                       TechnicalIndicators.MACD.determine_divergence_signal(prices[long - 1:], macd),
                       TechnicalIndicators.MACD.determine_dramatic_rise_signal(long_ma, short_ma),
                       TechnicalIndicators.MACD.determine_centerline_signal(macd))

        @staticmethod
        def determine_crossover_signal(macd, signal_ma):
            """

            :param macd:
            :param signal_ma:
            :return:
            """
            return [Signals.BUY if macd[index] > signal_ma[index] else
                    Signals.SELL if macd[index] < signal_ma[index] else
                    Signals.NEUTRAL for index in range(len(macd))]

        @staticmethod
        def determine_divergence_signal(prices, macd):
            """

            :param prices:
            :param macd:
            :return:
            """
            return [Signals.BUY if prices[index] < min(prices[:index + 1]) and macd[index] > min(macd[:index + 1])
                    else Signals.SELL if prices[index] > max(prices[:index + 1]) and macd[index] < max(macd[:index + 1])
                    else Signals.NEUTRAL for index in range(len(prices))]

        @staticmethod
        def determine_dramatic_rise_signal(long, short):
            """

            :param long:
            :param short:
            :return:
            """
            return [Signals.BUY if abs(short[index] - long[index]) < abs(short[index - 1] - long[index - 1]) else
                    Signals.SELL if abs(short[index] - long[index]) > abs(short[index - 1] - long[index - 1]) else
                    Signals.NEUTRAL for index in range(1, len(long))]

        @staticmethod
        def determine_centerline_signal(macd):
            """

            :param macd:
            :return:
            """
            return [Signals.BUY if macd[index] > 0 else
                    Signals.SELL if macd[index] < 0 else
                    Signals.NEUTRAL for index in range(len(macd))]

        @staticmethod
        def compute_macd(prices, long, short):
            """

            :param prices:
            :param long:
            :param short:
            :param signal:
            :return:
            """
            if len(prices):
                long_ma = TechnicalIndicators.MACD.compute_long_ma(prices, long)
                short_ma = TechnicalIndicators.MACD.compute_short_ma(prices[long - short:], short)
                return [short_ma[index] - long_ma[index] for index in range(len(long_ma))]

        @staticmethod
        def compute_long_ma(prices, long, weight_function=WeightFunctions.identity):
            """

            :param prices:
            :param long:
            :param weight_function:
            :return:
            """
            return TechnicalIndicators.MovingAverages.compute_weighted_moving_average(prices, long, weight_function)

        @staticmethod
        def compute_short_ma(prices, short, weight_function=WeightFunctions.identity):
            """

            :param prices:
            :param short:
            :param weight_function:
            :return:
            """
            return TechnicalIndicators.MovingAverages.compute_weighted_moving_average(prices, short, weight_function)

        @staticmethod
        def compute_signal_ma(prices, signal, weight_function=WeightFunctions.identity):
            """

            :param prices:
            :param signal:
            :param weight_function:
            :return:
            """
            return TechnicalIndicators.MovingAverages.compute_weighted_moving_average(prices, signal, weight_function)

