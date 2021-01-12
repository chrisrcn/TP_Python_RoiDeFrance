# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import csv
import json 
from pathlib import Path
import re

#Ouverture et Lecture du CSV 
with open('departements-france.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    code_region = 0
    for row in csv_reader:
        # Création de dossiers Région
        code_region = row["code_region"]
        if not os.path.exists(row["nom_region"]):
            os.makedirs(row["nom_region"])
        # print(os.listdir('.'))
        for element in os.listdir('.'):
            # Création de dossiers département associés à leur région
            if element == row["nom_region"]:
                if not os.path.exists(row["nom_region"] + '/' +row["nom_departement"]):
                    os.chdir(element)
                    os.makedirs(row["nom_departement"])
                    os.chdir('..')

#Ouverture et lecure du fichier JSON
with open('liste-des-immeubles-proteges-au-titre-des-monuments-historiques.json') as jsonfile:
    monuments = json.load(jsonfile)
    for row in monuments:
        #Variable contenant ce qu'il y a dans la clé tico et la reformate en bon éduforme
        tico = row["fields"]["tico"].replace("\'"," ")
        #créer une regex permettant de relever les noms de roi dans les != noms de monument
        def stringRoi(strTico):
            match = re.search('Hugues|Robert|Henri|Philippe|Louis|Jean|Charles', strTico)
            if match:
                result = True
            else:
                result = False                
            return result
        try:
            #Vérification regex 
            if stringRoi(tico) is True:
                if 'dpt_lettre' in row["fields"]:
                    #Ecriture des fichiers txt
                    fichier = open("./" + row["fields"]["reg"] + "/" + row["fields"]["dpt_lettre"] + "/" + tico + ".txt", "wt")
                    fichier.writelines(row["fields"]["reg"])
                    fichier.close()
        except Exception:
            pass

    

                    

