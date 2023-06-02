<<<<<<< HEAD
class CallDataRest :
    def __init__(self,json_file ):
        self.json_file = json_file


    def match_param_query_next_pass(self, input_station,input_line) :
        for i in range(len(self.json_file)) :
            if (input_station == self.json_file[i]["fields"]['nom_zdl']) and (input_line == self.json_file[i]["fields"]['ligne']) :
                return f'STIF:StopArea:SP:{int(self.json_file[i]["fields"]["id_ref_lda"])}:', f'LineRef=STIF:Line::{self.json_file[i]["fields"]["idrefligc"]}:'
=======
from ClassData.DataClassAPI import  GetDataAPI, GetDataFile
import requests
import json
import pandas as pd
import dateutil

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
            if ((self.input_station == arrets_ligne[i]["fields"]['nom_zdl']) or (self.input_station == arrets_ligne[i]["fields"]['nom_iv'])) and (self.input_line == arrets_ligne[i]["fields"]['ligne']) :
                return f'STIF:StopArea:SP:{int(arrets_ligne[i]["fields"]["id_ref_lda"])}:', f'STIF:Line::{arrets_ligne[i]["fields"]["idrefligc"]}:'

    def url_res(self) :
        param = self.url_param() #CallDataRest(arrets_ligne).match_param_query_next_pass(input_station,input_line)
        print(param[0],param[1])
        url = f"https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef={param[0]}&LineRef={param[1]}"

        return self.res(url)

    def next_pass(self):
        next_pass_info = self.url_res()
        #print(next_pass_info)

    #get api info
        l = []
        for i in range(len(next_pass_info[list(next_pass_info.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"])) :
            """
            corriger cette condition car certaines requetes (input_station =  "Crécy-la-Chapelle" ; input_line =   "TRAIN P")  ne renvoient  rien
            """
            api_info_filtered = next_pass_info[list(next_pass_info.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][i]["MonitoredVehicleJourney"]["MonitoredCall"]
            l.append(api_info_filtered)

        #api_info to pd.df
        # l2 = []
        # for i,j in enumerate(l) :
        #     if j["VehicleAtStop"] == True :
        #         print(j)
        #         l2.append(j.values())
        #print(l)
        df = pd.DataFrame(l, columns=['StopPointName', 'VehicleAtStop', 'DestinationDisplay', 'ExpectedArrivalTime', 'ExpectedDepartureTime', 'DepartureStatus', 'ArrivalStatus'])
        df.dropna(subset=['ExpectedArrivalTime', 'ExpectedDepartureTime'], inplace=True)

        #Clean df
        df.StopPointName = df.StopPointName.map(lambda v:  "".join(v[0].values()))
        df.DestinationDisplay = df.DestinationDisplay.map(lambda v:  "".join(v[0].values()))

        df.ExpectedArrivalTime = df.ExpectedArrivalTime.map(lambda d : f'{dateutil.parser.parse(d).time().hour+2}:{dateutil.parser.parse(d).time().minute}:{dateutil.parser.parse(d).time().second}') #time
        #print(df.ExpectedArrivalTime.map(lambda d : dateutil.parser.parse(d).date())) #date
        df.ExpectedDepartureTime = df.ExpectedDepartureTime.map(lambda d : f'{dateutil.parser.parse(d).time().hour+2}:{dateutil.parser.parse(d).time().minute}:{dateutil.parser.parse(d).time().second}') #time


        return df
"""
https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=%20STIF%3AStopPoint%3AQ%3A473921%3A&LineRef=STIF%3AStopArea%3ASP%3A474151%3A

"""



>>>>>>> dev
