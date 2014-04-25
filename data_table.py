__author__ = 'Modulus'


class Data(object):

    def __init__(self, start_date, end_date, name, data):
        self.start_date = start_date
        self.end_date = end_date,
        self.name = name
        self.data = data

    def json(self):
        return {
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "name": self.name,
            "numbers": self.data
        }