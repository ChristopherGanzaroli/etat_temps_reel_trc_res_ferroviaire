import sys
sys.path.append("..")
from ClassData.twitter import GetTweet #get_tweets

ligne = GetTweet("RER A").get_tweets()
print(ligne)
















# def match_patern_twitter_account_name(ligne) :
#
#     if "RER A" in ligne :
#         ligne = ligne.replace(" ", "_")
#
#     elif "RER B" in ligne :
#         ligne = ligne.replace(" ","")
#
#     elif ("RER C") or ("RER D") in ligne :
#         ligne = ligne.replace(f"RER {ligne[4]}",f"RER{ligne[4]}_SNCF")
#
#     elif "METRO" in ligne :
#         ligne = ligne.replace(f"METRO {ligne[6]}",f"Ligne{ligne[6]}_RATP")
#
#     if  ligne in ["TRAIN L", "TRAIN P", "TRAIN H","TRAIN R","TRAIN J", "TRAIN K"]  :
#         ligne = ligne.replace(f"TRAIN {ligne[6]}",f"Ligne{ligne[6]}_SNCF")
#
#     if ligne in ["TRAIN N", "TRAIN U"] :
#         ligne = ligne.replace(f"TRAIN {ligne[6]}",f"LignesNetU_SNCF")
#
#     return ligne






# df_feltred = pd.DataFrame(get_tweets(match_patern_twitter_account_name(ligne)))
# #dt = df_feltred.to_dict('records')
# print(df_feltred)


#print(data.to_dict('records'))

# for i in range(len(data)) :
#
#     d = {
#     'Date':data.Date[i],
#     'User' : data.User[i],
#     'Tweet':data.Tweet[i]}
#     print(d)















# from kafka import KafkaProducer
# import json
# #from data import get_registered_user
# import time
# import requests
#
# url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=-1&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
# r = requests.get(url)
# data = r.json()
# data = data["records"]
# def get_registered_user():
#
#     for i in range(len(data)):
#         data[i]['fields']['name']
#
# def json_serializer(data):
#     return json.dumps(data).encode("utf-8")
#
# producer = KafkaProducer(bootstrap_servers=['192.168.1.14:9092'],
#                          value_serializer=json_serializer)
#
# if __name__ == "__main__":
#     while 1 == 1:
#         registered_user = get_registered_user()
#         print(registered_user)
#         producer.send("registered_user", registered_user)
#         time.sleep(0.1)