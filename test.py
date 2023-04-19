import sys
sys.path.append("..")
from ClassData.twitter import GetTweet #get_tweets
from ClassData.DataClassAPI import GetDataFile, GetDataAPI
from ClassData.ApiResquest import NextPass
import pandas as pd
import json
import requests
import dateutil
from  datetime import datetime
import datetime as dt
import pendulum





#########################################################################################################################################
## [TEST]
## NEXT_PASS
#########################################################################################################################################
df_horaire = GetDataFile(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\test_stop_times.csv").csv_file(sep=";")
station_file = GetDataFile(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\emplacement-des-gares-idf.json").json_input()

# print(arrets_ligne["Geo Point"].str.split(',', expand=True)[1])

input_station = "Vincennes" #input("Entrer station ") #Ch\u00e2telet - Les Halles
input_line = "RER A"#input("Entrer station ") #RER A

input_station =  "Esbly"   #"Houilles-Carrières-sur-Seine" #input("Entrer station ") #Ch\u00e2telet - Les Halles
input_line =   "TRAIN P"     #"TRAIN L"#input("Entrer station ") #RER A

# for i in range(len(station_file)):
#     if input_station == station_file[i]["fields"]["nom_iv"] :
#         print(station_file[i]["fields"]["nom_zdl"])
test = NextPass(input_station,input_line).next_pass()
print(test)




#########################################################################################################################################
## [TEST]
## MAIN <- MAP
#########################################################################################################################################

# arrets_ligne  = pd.DataFrame(GetDataFile(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\emplacement-des-gares-idf.csv").csv_file(sep=";"))
# arrets_ligne["lat"] = arrets_ligne["Geo Point"].str.split(',', expand=True)[0].astype(float)
# arrets_ligne["lon"] = arrets_ligne["Geo Point"].str.split(',', expand=True)[1].astype(float)
# input_station = "Houilles-Carrières-sur-Seine" #input("Entrer station ") #Ch\u00e2telet - Les Halles
# input_line = "TRAIN L"#input("Entrer station ") #RER A
# import plotly.express as px
# import dash
# from dash import Dash, dcc, html, Input, Output
# import plotly.io as pio
# import plotly.graph_objects as go
#
# pio.templates.default = "plotly_dark"
#
# px.set_mapbox_access_token(open(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\app\mapbox_token.txt").read())
# df = px.data.carshare()
# fig = px.scatter_mapbox(arrets_ligne, lat="lat", lon="lon",     color="ligne",
#                          color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
# #fig.show()
# #map_filtered_test.to_excel("map_filtered_test.xlsx")
#
#
# app = dash.Dash()
# app.layout = html.Div(
#
#     className='DD_div',
#     children=[
#
#         dcc.Dropdown(
#         id='DD_name_ligne_input',
#         options=
#         [dict(label=x, value=x)
#          for x in arrets_ligne["ligne"].unique()],
#             placeholder="Selectionnez une station"),
#
#         dcc.Dropdown( #Dropdown station
#         id='DD_name_station_input',
#         options=
#         [dict(label=x, value=x)
#          for x in arrets_ligne["nom"].unique()],
#         placeholder="Selectionnez une station"),
#
#         html.Div([dcc.Graph(id="map_output1")])
#
#
#          #[dcc.Graph(id="map_output")]
#     ]
#
# )
#
#
#
# @app.callback(
#     Output('map_output1', 'figure'),
#
#     Input('DD_name_ligne_input',"value")
#     #Input('DD_name_station_input',"value")
# )
# def update_graph(DD_name_ligne_input):
#         px.set_mapbox_access_token(open(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\app\mapbox_token.txt").read())
#         df =  arrets_ligne.copy()
#
#         if not DD_name_ligne_input :
#             fig = px.scatter_mapbox(df, lat="lat", lon="lon",     color="ligne",
#                                     color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
#             return fig
#         else :
#             df =  arrets_ligne[arrets_ligne.ligne == DD_name_ligne_input]
#             fig = px.scatter_mapbox(df, lat="lat", lon="lon",     color="ligne",
#                                     color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
#             return fig
#
#
#
#
# app.run_server(debug=True, use_reloader=True, port=8053)





















#
#
#

"""
ID commun
NexPass : 'id_ref_zdl': 43166
stop_times[stop_id] = IDFM:monomodalStopPlace:43166

"""
#Destination
#print(test[list(test.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][1]["MonitoredVehicleJourney"]['DestinationName'])
#Horaire

#get api info
# l = []
# for i in range(len(test[list(test.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"])) :
#     t = test[list(test.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][i]["MonitoredVehicleJourney"]["MonitoredCall"]
#     l.append(t)
#
# #transformation df
# l2 = []
# for i,j in enumerate(l) :
#     l2.append(j.values())
#
# df = pd.DataFrame(l, columns=['StopPointName', 'VehicleAtStop', 'DestinationDisplay', 'ExpectedArrivalTime', 'ExpectedDepartureTime', 'DepartureStatus', 'ArrivalStatus'])

#Clean df
#print(df.StopPointName.map(lambda v:  "".join(v[0].values())))
#print(df.DestinationDisplay.map(lambda v:  "".join(v[0].values())))
#print(df.ExpectedArrivalTime.map(lambda d : dateutil.parser.parse(d).time())) #time
#print(df.ExpectedArrivalTime.map(lambda d : dateutil.parser.parse(d).date())) #date
#print(df.ExpectedDepartureTime.map(lambda d : dateutil.parser.parse(d).time()))

#
# def info():
#     next_pass_info = NextPass(input_station,input_line).url_res()
#
#     #get api info
#     l = []
#     for i in range(len(next_pass_info[list(next_pass_info.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"])) :
#         api_info_filtered = next_pass_info[list(next_pass_info.keys())[0]]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"][i]["MonitoredVehicleJourney"]["MonitoredCall"]
#         l.append(api_info_filtered)
#
#     #api_info to pd.df
#     l2 = []
#     for i,j in enumerate(l) :
#         l2.append(j.values())
#
#     df = pd.DataFrame(l, columns=['StopPointName', 'VehicleAtStop', 'DestinationDisplay', 'ExpectedArrivalTime', 'ExpectedDepartureTime', 'DepartureStatus', 'ArrivalStatus'])
#
#
#     #Clean df
#     df.StopPointName = df.StopPointName.map(lambda v:  "".join(v[0].values()))
#     df.DestinationDisplay = df.DestinationDisplay.map(lambda v:  "".join(v[0].values()))
#     df.ExpectedArrivalTime = df.ExpectedArrivalTime.map(lambda d : f'{dateutil.parser.parse(d).time().hour+2}:{dateutil.parser.parse(d).time().minute}:{dateutil.parser.parse(d).time().second}') #time
#     #print(df.ExpectedArrivalTime.map(lambda d :  dt.timedelta(hours=d.hour+2)))
#     #print(df.ExpectedArrivalTime.map(lambda d :  f'{d.hour+2}:{d.minute}:{d.second}'))
#     #print(df.ExpectedArrivalTime.map(lambda d : dateutil.parser.parse(d).date())) #date
#     df.ExpectedDepartureTime = df.ExpectedDepartureTime.map(lambda d : dateutil.parser.parse(d).time())
#
#     return df
#
# print(info())



















#
# ligne = GetTweet("METRO 2").get_tweets()
# print(ligne)
















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