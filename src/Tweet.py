from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer

class Tweet:
    def __init__(self, date, message):
        #Remove the annoying stylized quote marks and replace them with regular ones
        message = message.replace('“','"') 
        message = message.replace('”','"')
        
        self.date = date
        self.message = message
        self.sentiment = self.__calc_sentiment()

    def __calc_sentiment(self):
        sia = SentimentIntensityAnalyzer()
        return sia.polarity_scores(self.message)['compound']