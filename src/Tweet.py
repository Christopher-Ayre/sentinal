from datetime import datetime

class Tweet:
    def __init__(self, date, message):
        self.date = date
        self.message = message
        self.sentiment = self.__calc_sentiment()

    def __calc_sentiment(self):
        return 1