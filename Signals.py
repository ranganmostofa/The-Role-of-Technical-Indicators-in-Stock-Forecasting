from enum import Enum


class Signals(Enum):
    """

    """
    BUY = 1
    SELL = -1
    NEUTRAL = 0

    @staticmethod
    def to_signal(value):
        """

        :param value:
        :return:
        """
        return Signals.BUY if value > 0 else Signals.SELL if value < 0 else Signals.NEUTRAL

