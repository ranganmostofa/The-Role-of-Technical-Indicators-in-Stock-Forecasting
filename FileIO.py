import csv


class FileIO:
    """

    """
    @staticmethod
    def read_csv(csv_filename):
        """
        :param csv_filename:
        :return:
        """
        csv_matrix = []
        with open(csv_filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                csv_matrix.append(list(row))
        return csv_matrix

    @staticmethod
    def write_csv(csv_filename, data_matrix):
        """"
        :param csv_filename:
        :param data_matrix:
        :return:
        """
        with open(csv_filename, "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            for row in data_matrix:
                csv_writer.writerow(list(row))

