from random import randrange


class DataProcessing:
    """

    """
    @staticmethod
    def extract_prices(data_matrix, *fields):
        """

        :param data_matrix:
        :return:
        """
        prices = list()
        tupled_values = zip(*[DataProcessing.extract_field(data_matrix, field_name) for field_name in fields])
        for tupled_value in tupled_values:
            prices += list(tupled_value)
        return prices

    @staticmethod
    def extract_field(data_matrix, field_name):
        """

        :param data_matrix:
        :param field_name:
        :return:
        """
        return DataProcessing.map_transform(data_matrix)[field_name]

    @staticmethod
    def map_transform(data_matrix):
        """

        :param data_matrix:
        :return:
        """
        return {field_name: field_values for (field_name, field_values) in [(row[0], row[1:])
                                                    for row in DataProcessing.compute_matrix_transpose(data_matrix)]}

    @staticmethod
    def compute_matrix_transpose(matrix):
        """

        :param matrix:
        :return:
        """
        if len(matrix):
            transpose = [list() for _ in range(len(matrix[randrange(len(matrix))]))]
            for row in matrix:
                for index in range(len(row)):
                    transpose[index].append(row[index])
            return transpose
        return matrix

