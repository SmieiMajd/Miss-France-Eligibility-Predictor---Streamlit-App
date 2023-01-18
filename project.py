import streamlit as st 
import pandas as pd
import os 
from PIL import Image
import base64
import streamlit as st 
import pandas as pd
import os 
from PIL import Image
import base64
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import pickle

st.set_page_config(layout="wide")
#Creation fichier.csv
infos ={} 
path = 'D:/miss/miss_fr.csv'
selection_model = 'selection_model.pkl'      

def save_infos_csv(infos, path):
  df = pd.DataFrame(infos, index=[0]) 
  file_found = os.path.exists(path)
  if(file_found):
    df.to_csv(path, mode='a', header=False, index=False)
  else:
    df.to_csv(path, header=True, index=False)
    
#background image 
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 100%
        
       
       
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('miss.png') 





st.title("Miss France 22 : Préselection")
#les champs de Form           
def form():
    st.header("Veuillez faire vos inscriptions avant le 30/12 ")
    with st.form(key="Information form",clear_on_submit=True):
        nom = st.text_input("Entrer votre nom:")
        infos["nom"]=nom
        prenom= st.text_input("Entrer votre prenom:")
        infos["prenom"]=prenom
        occupation =st.selectbox("Occupation",["Etudiante","Travail:temps plein","Travail:temps partiel"])
        infos["occupation"]= occupation
        age =st.number_input("Entrer votre Age:", min_value=18, max_value=30, value=24, step=1)
        infos["age"]= age
        taille =st.number_input("Entrer votre taille:", min_value=1.50, max_value=1.99, value=1.55, step=0.01)



        
        infos["taille"]= taille
        poids =st.number_input("Entrer votre poids:", min_value=45.0, max_value=75.0, value=53.0, step=0.1)
        infos["poids"]= poids
        
        options = st.multiselect(
       'Quelles langues maitriez vous',
        ['Arabe', 'Anglais', 'Allemand', 'Italien', 'Espagnool', 'Potiugais'])

        
        
        infos["options"]= len(options)
        
        genre = st.radio(
        "Indiquez l'origine de vos parents",
        ('La France', 'Europe (autre que la France)', 'Asie', 'Afrique', 'Amerique' ))
        if genre == 'La France':
         st.write('Vous étes Française.')
        else:
         st.write('Vous nétes pas Française.')

        infos["genre"]= genre
        
        
        df1 = pd.DataFrame([infos])
        lab = LabelEncoder()
        lab.fit_transform(df1['occupation'])
        label_mapping = {"Travail:temps plein": 0, "Travail:temps partiel": 1, "Etudiante": 2}
        df1['occup']=df1['occupation']
        df1 = df1.replace({"occup": label_mapping})
        X=df1.drop(['nom','prenom','occupation','genre'],axis=1)
        with open(selection_model, 'rb') as file:
            prediction_model = pickle.load(file)
        y_pred = prediction_model.predict(X)
        label=y_pred[0]
        infos["label"]= label
        
        submission = st.form_submit_button(label="Enregistrer")
        if submission == True:
            save_infos_csv(infos, path)
            st.success("Salut {} Enregsitrement Valide".format(nom))
form()    
