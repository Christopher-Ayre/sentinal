class Coin:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol
        self.favour = None
        self.tweets = []

    def add_tweet(self,tweet):
        if tweet not in self.tweets:
            self.tweets.append(tweet)
            self.calc_favour()

    def calc_favour(self):
        favour = 0.0
        for tweet in self.tweets:
            favour += tweet.sentiment

        self.favour = favour