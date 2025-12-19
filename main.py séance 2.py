#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)
    
# Mettre dans un commentaire le numéro de la question
# Question 5
print(pd.DataFrame(contenu))
# Question 6
print("nombre de ligne", contenu.line)
print("nombre de colonne", contenu.columns)