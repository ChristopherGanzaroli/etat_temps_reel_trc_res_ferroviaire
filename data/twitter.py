import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime

start_date = datetime.datetime.now()

def get_tweets(username):
    query = f"(from:{username}), since:{start_date:%Y-%m-%d} lang:fr" #until:2023-09-04 since:2023-09-03"
    tweets = []
    limit = 3
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user, tweet.rawContent])

    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    print(df)
get_tweets("RER_A") #RER_A Ligne1_RATP