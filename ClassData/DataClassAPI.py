import json
import requests

class GetDataAPI:
    """
    Class récupération data
    """
    global headers
    headers= {'Accept': 'application/json', 'apikey': 'ZTckQPr4yBB7roJMCMBbQLS9OKmXbW9P'}
    def __init__(self, url):                # url recupérée lors de l'initialisation de l'objet
        self.url = url

###################################################################################################
##   Récupération des données au format json                                                     ##
###################################################################################################
    def json_data(self):
        r = requests.get(self.url)
        json_data = r.json()
        return json_data
###################################################################################################
##   Récupération des données au format tableay                                                  ##
###################################################################################################
    def array_data(self):
        r = requests.get(self.url)
        array_data = r
        return array_data

###################################################################################################
##   Récupération les horaires d'arrivéé                                                         ##
##   https://prim.iledefrance-mobilites.fr/fr/donnees-dynamiques/idfm-ivtr-requete_unitaire      ##
###################################################################################################


    def next_pass(self):
        r = requests.get(self.url, headers=headers)
            #Affichage du code réponse
        #print('Status:',r)
        #Affichage du contenu de la réponse
        #print(r.content)



###################################################################################################
##   Récupération d'une clé dans un dictionnaire                                                 ##
###################################################################################################
class GetDataFil :
    def __init__(self, path) :
        self.path = path


    def json_input(self):
        with open(self.path, "r") as f :
            return json.loads(f.read())
    def iter_(self, key):
        self.json_input()
        return [i[key] for i in self.json_input().iteritems()]



