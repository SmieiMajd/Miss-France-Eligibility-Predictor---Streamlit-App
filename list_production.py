import random 
import os
import pandas as pd

infos ={} 
path = 'D:/miss/miss_fr.csv'      
def save_infos_csv(infos, path):
  df = pd.DataFrame(infos, index=[0]) 
  file_found = os.path.exists(path)
  if(file_found):
    df.to_csv(path, mode='a', header=False, index=False, encoding='utf-8')
  else:
    df.to_csv(path, header=True, index=False, encoding='utf-8')
    
noms = ["SNAVELY","DE SAXE","DE BAVIERE","DE SAVOIE","MALTAIS","DE HALLUIN","GAUDREAULT","DE VERMANDOIS","DE HALLEWIN","SNIVELY","DE NORMANDIE","DE HAINAUT","D ANGLETERRE","DE PROVENCE","D AQUITAINE","SCHNEBLI","DE FRANCIE","DE CASTILLE","WUETRICH","DE LUXEMBOURG","DE MONTMORENCY","DE ROME","DE TOULOUSE","DE COLOGNE","DE WISIGOTHIE","BUJOLD","D eGYPTE","GOBEIL","DE MONTCLAR","DE DANEMARK","D ALeMANIE","D ANGOULEME","LACHARITe","CAROLINGIEN","D AUTRICHE","D AUSTRASIE","BOULIANNE","DE COURTENAY","DE GASCOGNE","DE CHAMPAGNE","DE NAVARRE","DE BURGONDIE","DE THURINGE","DE LOMBARDIE","DE TOXANDRIE","DE ROHAN","SANDOZ GENDRE","DE LIMOGES"]
prenoms = ["Jade","Louise","Emma","Ambre","Alice","Rose","Anna","Lina","Lena","Chloe","Julia","Lou","Lea","InEs","Agathe","Iris","Zoe","Eva","Juliette","Leonie","Jeanne","AdEle","Victoire","Olivia","Victoria","Lucie","Margaux","Romane","Camille","Charlotte","Alix","Margot","Sarah","Manon","Capucine","Elise","Clemence","Clara","Gabrielle","Apolline","Celeste","Zelie","Albane","Lise","Maria","Mathilde","Eleonore","Thais","Anais","Heloise","Daphne","Isaure","AngEle","Line","Aline","Rosalie","Violette","Brune","Elisabeth","Clarisse","Abigaelle","Eve","Blanche","Lucile","Esther","Athenais","Noelie","Colette","SolEne","Luce","Berenice","Lyne","Philippine","Celine","Adelaide","Morgane","Eugenie","Sibylle","Marion","Lydia","Abigail","Amelie","HelEne","Sixtine","Estelle","Aimee","Claire","Marilou","Bertille","Melodie","Amandine","Prune","Flore","Fleur","Marianne","Adelie","Grace","Marylou","Flavie","Penelope","Coralie","Audrey","Suzon","Artemis","Auriane","Ambrine","Emmanuelle","Stephanie","Hermione","Marine","Eglantine","Tatiana","Armance","Cyrielle","Angeline","Tiphaine","Laureline","Hermine","Ludivine","Theodora","Laetitia","Eulalie","Solenn","France","Auxane","Adeline","Blandine","Nathalie","Marceline","MylEne","Barbara","LaurEne","Evangeline","Gwenaelle","Florine","Armelle","Aglae","Catherine","Aure","Seraphine","Eliane","Jacinthe","Angelique","Aubane","Alexine","Fantine","Lauriane","Aude","Ysaline"]
occupations =["Etudiante","Travail:temps partiel"]
ages=[y for y in range(22, 28)]
tailles = [x / 100 for x in range(165, 185)]
poidss=[z for z in range(46, 69)]
optionss=[w for w in range(3,6)]
genres=['La France', 'Europe (autre que la France)', 'Asie', 'Afrique', 'Amerique']

for i in range(1,800):
    nom=random.choice(noms)
    prenom=random.choice(prenoms)
    occupation=random.choice(occupations)
    age=random.choice(ages)
    taille=random.choice(tailles)
    poids=random.choice(poidss)
    options=random.choice(optionss)
    genre=random.choice(genres)

    if options <=2 or occupation =="Travail:temps plein" or taille < 1.6 or taille >= 1.9  or age > 28 or age < 20 or poids < 45 or poids > 70 :
        label= 0 
    else :
        label =1

    infos["nom"]=nom
    infos["prenom"]=prenom
    infos["occupation"]= occupation
    infos["age"]= age
    infos["taille"]= taille
    infos["poids"]= poids   
    infos["options"]= options 
    infos["genre"]= genre
    infos["label"]= label

    save_infos_csv(infos, path)
    