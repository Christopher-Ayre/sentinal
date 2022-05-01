from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer

class Tweet:
    def __init__(self, date, message):
        self.date = date
        message = message.replace('“','"') #Get rid of this shit
        message = message.replace('”','"')
        self.message = message
        self.sentiment = self.__calc_sentiment()

    def __calc_sentiment(self):
        sia = SentimentIntensityAnalyzer()
        return sia.polarity_scores(self.message)['compound']