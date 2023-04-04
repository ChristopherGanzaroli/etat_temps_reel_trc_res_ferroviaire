import json
import requests
from datetime import datetime
from time import sleep
import os
import sys
sys.path.append("..")
path_pwd = os.getcwd()
from ClassData.DataClassAPI import  GetDataAPI


############################################################################################################
####### Arrêts et lignes associées                                                                   #######
############################################################################################################
url_arrets_stions = "https://data.iledefrance-mobilites.fr/explore/embed/dataset/arrets-lignes/table/"
arrets_stations = GetDataAPI(url_arrets_stions).array_data()
print(arrets_stations)

############################################################################################################
####### Arrêts et lignes associées                                                                   #######
############################################################################################################
next_pass_url = 'https://prim.iledefrance-mobilites.fr/marketplace/general-message?LineRef=STIF%3ALine%3A%3AC01727%3A'
next_pass = GetDataAPI(next_pass_url).next_pass()


