import json
import requests
from datetime import datetime
from time import sleep
import os
import sys
sys.path.append("..")
path_pwd = os.getcwd()
from ClassData.DataClassAPI import  GetDataAPI, GetDataFile
from ClassData.ApiResquest import CallDataRest


############################################################################################################
####### Arrêts et lignes associées                                                                   #######
############################################################################################################

#next_pass = GetDataAPI(next_pass_url).next_pass()


############################################################################################################
####### Arrêts et lignes associées                                                                   #######
############################################################################################################

arrets_ligne  = GetDataFile(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\emplacement-des-gares-idf.json").json_input()
#Récupération l'arrid pour filtrer next_pass_url



input_station = "Vincennes" #input("Entrer station ") #Ch\u00e2telet - Les Halles
input_line = "RER A"#input("Entrer station ") #RER A
# def client_next_pass(input_station,input_line) :
#     param_next_pass = CallDataRest(arrets_ligne).match_param_query_next_pass(input_station,input_line)
#     next_pass_url = f"https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef={param_next_pass[0]}&{param_next_pass[1]}"
#     print(param_next_pass[0],param_next_pass[1])
#     return GetDataAPI(next_pass_url).next_pass()

test = CallDataRest(arrets_ligne,input_station,input_line).next_pass()
print(test)
#print(test[list(test.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0])