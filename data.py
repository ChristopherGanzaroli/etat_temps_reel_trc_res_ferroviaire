# import json
# import requests
#
#
# url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=-1&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
# r = requests.get(url)
# data = r.json()
# data = data["records"][-1]["fields"]
# print(data["name"])
# def get_velib_data(data):
#     return{data}