import os
import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from Tweet import Tweet
from Coin import Coin
import string
import re

def get_x_user_tweets(username, limit):
    #Use snscrape to get the last <limit> tweets from the <user>
    tweets = []
    os.system('snscrape --jsonl --progress --max-results ' + str(limit) + ' twitter-user ' + username + ' > user-tweets.json')
    with open('user-tweets.json') as f:
        lines = f.readlines()

    for line in lines:
        data = json.loads(line)
        tweets.append(Tweet(datetime.fromisoformat(data['date']),data['content'].replace('&amp;','and')))

    return tweets

def get_user_tweets_since(username, time):
    #Use snscrape to get tweets since <limit> from the <user>
    print('Getting tweets from @{0} since {1}'.format(username,time))
    tweets = []
    os.system('snscrape --jsonl --progress --since ' + str(time) + ' twitter-user ' + username + ' > user-tweets.json')
    with open('user-tweets.json') as f:
        lines = f.readlines()
    print('Scraped {0} tweets from user'.format(len(lines)))
    for line in lines:
        data = json.loads(line)
        #Remove timezone from string
        date_string = data['date'].split('+')[0] 
        date = datetime.strptime(date_string,'%Y-%m-%dT%H:%M:%S')
        tweets.append(Tweet(date,data['content'].replace('&amp;','and')))

    return tweets

def match_tweets_to_coins(tweets,coins):
    print('Matching Tweets to Coins:')
   
    #Seperate out only the tweets that contain our coin
    for i, tweet in enumerate(tweets):
        #Remove punctuation from message
        clean_message = re.sub('[.,@"!?\\-]','',tweet.message)
        for coin in coins:
            #Search word for word in the message looking for our coin
            for word in clean_message.split():
                if word == coin.symbol or word == coin.name:
                    coin.add_tweet(tweet)

#COULD ALSO WRITE ANOTHER FUNCTION THAT GETS A MANUAL COIN FILE TO AVOID THE STUPID MATCHES
def get_coins_from_whitelist(whitelist):
    coins = []
    with open(whitelist) as file:
        lines = file.readlines()
        for line in lines:
            name = line.split(',')[0].strip()
            symbol = line.split(',')[1].strip()
            coins.append(Coin(name,symbol))

    print('Read {0} coins from {1}'.format(len(coins),whitelist))
    return coins

def get_all_coins():
    #Slower to get from api than csv file on disk but they handle updating the list for us
    coins = []
    url = 'https://www.cryptocompare.com/api/data/coinlist/'
    print("Grabbing coins from: {0}".format(url))
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = json.loads(soup.prettify())
    data = data['Data']
    
    print('Filtering through blacklist')
    with open('../libs/Blacklist') as file:
        csv = file.read()
        blacklist = csv.split(",")

        for entry in data:
            name = data[entry]['CoinName']
            symbol = data[entry]['Symbol']
            if symbol not in blacklist and symbol.lower() not in blacklist and len(symbol) > 2:
                coins.append(Coin(name,symbol))

    print('Fetched ' + str(len(coins)) + ' coins')
    return coins