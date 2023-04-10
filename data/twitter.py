import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime

start_date = datetime.datetime.now()

def get_tweets(username):
    query = f"(from:{username}), since:{start_date:%Y-%m-%d} lang:fr" #until:2023-09-04 since:2023-09-03"
    tweets = []
    limit = 2
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user, tweet.rawContent])
            #tweets.append(["date", "user", "tweet"])

    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    return  df
