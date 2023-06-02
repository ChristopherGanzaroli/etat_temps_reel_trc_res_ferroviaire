import json
import requests
import pandas as pd

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


<<<<<<< HEAD
    def next_pass(self):
        r = requests.get(self.url, headers=headers)
            #Affichage du code réponse
        #print('Status:',r)
        #Affichage du contenu de la réponse
        return json.loads(r.content)
=======
    # def next_pass(self):
    #     r = requests.get(self.url, headers=headers)
    #         #Affichage du code réponse
    #     #print('Status:',r)
    #     #Affichage du contenu de la réponse
    #     return json.loads(r.content)
>>>>>>> dev



###################################################################################################
##   Récupération d'une clé dans un dictionnaire                                                 ##
###################################################################################################
class GetDataFile :
    def __init__(self, path) :
        self.path = path


    def json_input(self):
        with open(self.path, "r") as f :
<<<<<<< HEAD
            return json.loads(f.read())
=======
            #return json.loads(f.read())
            return json.loads(json.dumps(json.loads(f.read()), ensure_ascii=False)) #correction mauvais encordage du fichier
>>>>>>> dev
    def iter_(self, key):
        self.json_input()
        return [i[key] for i in self.json_input().iteritems()]

    def csv_file(self, sep):
        df = pd.read_csv(self.path, sep=sep)
        return df



