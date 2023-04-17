import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime

start_date = datetime.datetime.now()
class GetTweet :
    def __init__(self, ligne):
        self.ligne = ligne

    def match_patern_twitter_account_name(self) :

        if "RER A" in self.ligne :
            user_name = self.ligne.replace(" ", "_")

        elif "RER B" in self.ligne :
            user_name = self.ligne.replace(" ","")

        elif ("RER C") or ("RER D") in self.ligne :
            user_name = self.ligne.replace(f"RER {self.ligne[4]}",f"RER{self.ligne[4]}_SNCF")

        if "METRO" in self.ligne :

            user_name = self.ligne.replace(f"METRO {self.ligne[6]}",f"Ligne{self.ligne[6]}_RATP")
            print(self.ligne,user_name)

        if  self.ligne in ["TRAIN L", "TRAIN P", "TRAIN H","TRAIN R","TRAIN J", "TRAIN K"]  :
            user_name = self.ligne.replace(f"TRAIN {self.ligne[6]}",f"Ligne{self.ligne[6]}_SNCF")

        if self.ligne in ["TRAIN N", "TRAIN U"] :
            user_name = self.ligne.replace(f"TRAIN {self.ligne[6]}",f"LignesNetU_SNCF")

        return user_name

    def get_tweets(self):
        username = self.match_patern_twitter_account_name()
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
                #tweets.append(["date", "user", "tweet"])

        df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
        return  df




# def get_tweets(username):
#     query = f"(from:{username}), since:{start_date:%Y-%m-%d} lang:fr" #until:2023-09-04 since:2023-09-03"
#     tweets = []
#     limit = 3
#     for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#
#         # print(vars(tweet))
#         # break
#         if len(tweets) == limit:
#             break
#         else:
#             tweets.append([tweet.date, tweet.user, tweet.rawContent])
#             #tweets.append(["date", "user", "tweet"])
#
#     df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
#     return  df