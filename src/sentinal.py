#!/usr/bin/env python3
import sys
import scraper
from datetime import datetime
from Tweet import Tweet
from Coin import Coin

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Invalid Arguments, please give <TwitterHandle> <ScrapeLimit>")
    else:
        tweets = scraper.get_users_tweets(sys.argv[1],int(sys.argv[2]))
        coins = scraper.get_coins_from_whitelist('libs/Whitelist')
        scraper.match_tweets_to_coins(tweets,coins)

        print('RESULTS:')
        for coin in coins:
            #If there are any tweets connected to the coin
            if coin.tweets:
                print('##################################  ' + coin.symbol + '  ##################################')
                for tweet in coin.tweets:
                    print(tweet.message + '\n\n\n')