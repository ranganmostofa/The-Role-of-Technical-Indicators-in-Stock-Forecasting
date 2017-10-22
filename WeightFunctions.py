from math import exp


class WeightFunctions:
    """

    """
    @staticmethod
    def ones(*args):
        """

        :param args:
        :return:
        """
        if len(args) > 1:
            return [1 for _ in args]
        return 1

    @staticmethod
    def identity(*args):
        """

        :param args:
        :return:
        """
        if len(args) > 1:
            return [1 for _ in args]
        return [*args].pop()

    @staticmethod
    def exponential(*args):
        """

        :param args:
        :return:
        """
        if len(args) > 1:
            return [exp(arg) for arg in args]
        return exp(*args)

