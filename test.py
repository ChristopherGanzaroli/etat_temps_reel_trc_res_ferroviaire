import sys
sys.path.append("..")
from ClassData.DataClassAPI import GetDataFile


arrets_ligne  = GetDataFile(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\emplacement-des-gares-idf.csv").csv_file(sep=";")



print(float(["Geo Point"].str.split(',', expand=True)[0]))

















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