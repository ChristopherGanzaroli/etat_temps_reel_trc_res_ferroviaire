from ClassData.DataClassAPI import  GetDataAPI, GetDataFile
import requests
import json

class NextPass :

    global headers
    headers= {'Accept': 'application/json', 'apikey': 'ZTckQPr4yBB7roJMCMBbQLS9OKmXbW9P'}
    global arrets_ligne
    arrets_ligne  = GetDataFile(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\emplacement-des-gares-idf.json").json_input()

    def __init__(self,input_station,input_line ):
        self.input_station = input_station
        self.input_line = input_line

    def res(self,url):
        r = requests.get(url, headers=headers)
        return json.loads(r.content)


    def url_param(self) : #recherche les id ligne et station dans emplacement-des-gares-idf.json
        for i in range(len(arrets_ligne)) :
            if (self.input_station == arrets_ligne[i]["fields"]['nom_zdl']) and (self.input_line == arrets_ligne[i]["fields"]['ligne']) :
                return f'STIF:StopArea:SP:{int(arrets_ligne[i]["fields"]["id_ref_lda"])}:', f'LineRef=STIF:Line::{arrets_ligne[i]["fields"]["idrefligc"]}:'

    def next_pass(self) :
        param = self.url_param() #CallDataRest(arrets_ligne).match_param_query_next_pass(input_station,input_line)
        url = f"https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef={param[0]}&{param[1]}"
        print(param[0],param[1])
        return self.res(url)
"""
https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=%20STIF%3AStopPoint%3AQ%3A473921%3A&LineRef=STIF%3AStopArea%3ASP%3A474151%3A

"""



