#!/usr/bin/env python3
import sys
import scraper
from datetime import date, timedelta
from Tweet import Tweet
from Coin import Coin
import string

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Invalid Arguments, please give <TwitterHandle> <SinceDate>")
    else:
        date_limit = date.today() - timedelta(days=int(sys.argv[2]))
        tweets = scraper.get_user_tweets_since(sys.argv[1], date_limit)

        if tweets:
            coins = scraper.get_coins_from_whitelist('resources/Whitelist')
            scraper.match_tweets_to_coins(tweets,coins)

            print('RESULTS:')
            for coin in coins:
                #If there are any tweets connected to the coin
                if coin.tweets:
                    print(coin.symbol + ' : ' + str(coin.favour))
                    for tweet in coin.tweets:
                        print('\t{0} : {1}'.format(tweet.date.strftime("%d/%m/%Y,%H:%M:%S"),tweet.sentiment))
        
        else:
            print('No tweets found')