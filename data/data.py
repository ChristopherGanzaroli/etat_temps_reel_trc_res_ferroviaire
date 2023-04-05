import json
import requests
from datetime import datetime
from time import sleep
import os
import sys
sys.path.append("..")
path_pwd = os.getcwd()
from ClassData.DataClassAPI import  GetDataAPI, GetDataFil


############################################################################################################
####### Arrêts et lignes associées                                                                   #######
############################################################################################################
url_arrets_stions = "https://data.iledefrance-mobilites.fr/explore/embed/dataset/arrets-lignes/table/"
arrets_stations = GetDataAPI(url_arrets_stions).array_data()
#print(arrets_stations)

############################################################################################################
####### Arrêts et lignes associées                                                                   #######
############################################################################################################
next_pass_url = 'https://prim.iledefrance-mobilites.fr/marketplace/general-message?LineRef=STIF%3ALine%3A%3AC01727%3A'
next_pass = GetDataAPI(next_pass_url).next_pass()



############################################################################################################
####### Arrêts et lignes associées                                                                   #######
############################################################################################################

arrets_ligne  = GetDataFil(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\emplacement-des-gares-idf.json").json_input()
#Récupération l'arrid pour filtrer next_pass_url
input_station = input("Entrer station ") #Ch\u00e2telet - Les Halles
input_line = input("Entrer station ") #RER A
def match_query(json_file, input_station,input_line) :
    for i in range(len(json_file)) :
        if (input_station == json_file[i]["fields"]['nom_zdl']) and (input_line == json_file[i]["fields"]['ligne']) :
            print(f'STIF:StopArea:SP:{int(json_file[i]["fields"]["id_ref_lda"])}:', f'STIF:Line::{json_file[i]["fields"]["idrefligc"]}')

#print(match_line_code(arrets_ligne, 'route_long_name',input_test))
match_query(arrets_ligne,input_station,input_line)

