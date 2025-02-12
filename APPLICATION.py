
    import streamlit as st
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    from requests import get
    import base64
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import streamlit as st
    import streamlit.components.v1 as components
    
    
    
    
    st.markdown(<h1 style='text-align: center; color: black;'>SCARPER LES DONNEES</h1>, unsafe_allow_html=True)
    
    st.markdown("""
    Cette application effectue le webscraping des données de Coin Afrique sur plusieurs pages. 
    Et nous pouvons également télécharger les données extraites de l application directement sans les extraire. 
    * **Bibliothèques Python :** base64, pandas, streamlit, requests, bs4 
    * **Source des données :** https://sn.coinafrique.com/categorie/vetements-enfants --https://sn.coinafrique.com/categorie/chaussures-enfants.""")

                                                          #PARTIE 1
              # Fontion du background
    def add_bg_from_local(image_file):
       with open(image_file, \"rb\") as mage_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
    
        <style>
        .stApp {{
            background-image: url(data:image/{"webp"};base64,{encoded_string.decode()});
            background-size: cover
            }}
        </style>

        unsafe_allow_html=True
    
             # fond d'ecran de l'application
    add_bg_from_local("Fondecran.webp")
             # Scarper les données 
    @st.cache_data
    
    def convert_df(df):
    
        return df.to_csv().encode('utf-8')
    
    def load(dataframe, title, key, key1) :
        st.markdown(
        <style>
        div.stButton {text-align:center}
        </style>, unsafe_allow_html=True)
    
        if st.button(title,key1):
            
             st.subheader("Dimension") 
             st.write("Dimension des données:" + str(dataframe.shape[0]) +  rows and  + str(dataframe.shape[1]) + " columns.")
             st.dataframe(dataframe)
    
            csv = convert_df(dataframe)
    
            st.download_button(
                label="Télécharger les données en CSV"
                data=csv,
                file_name='Données.csv',
                mime='text/csv',
                key = key)
    
   # def local_css(file_name):
        #with open(file_name) as f:
            #st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
                                                                 # PARTIE 2 
            
                     # Fonction de scraping des données vetements des enfants
    def scrape_vetements_data(plusieurs_page):
        DF=pd.DataFrame()\
        for index in range(1, int(plusieurs_page)+1): 
            url=f'https://sn.coinafrique.com/categorie/vetements-enfants?page={index}'
            res= get(url)
            soup= bs(res.text, 'html.parser')
            containers= soup.find_all('div', class_="col s6 m4 l3")
            donne = []
    for container in containers :
        try :
             type_habits=container.find(\"p", class_="ad__card-description").text.strip()
             Prix=container.find("p", class_="ad__card-price").text.strip().replace("CFA", "" )
             Adresse=container.find("p", class_="ad__card-location").text.strip().replace("location_on", "")
             Image_lien=container.find("img",class_="ad__card-img")["src"]
            
             dic = {
                    "Type habits": type_habits,
                    "Prix": Prix,
                    "Adresse": Adresse,
                    "Image_lien": Image_lien,  
                }
             donne.append(dic)
        except :
               pass
    Df=pd.DataFrame(donne)
    DF= pd.concat([DF,Df], axis=0).reset_index(drop=True)
        return Df   
                                                            # PARTIE 3
    
    def scrape_chaussures_data(plusieurs_page):
        df=pd.DataFrame()
        for p_index in range (1,int(plusieurs_page)+1):
            url= f'https://sn.coinafrique.com/categorie/chaussures-enfants?page={p_index}'
            res= get( url)
            soup= bs(res.text, 'html.parser')
            Paquets= soup.find_all('div', class_="col s6 m4 l3")
            donne = []
    for Paquet in Paquets:
        try :
            
            Type_chaussures=Paquet.find("p", class_="ad__card-description").text.strip()
            Prix=Paquet.find("p",class_="ad__card-price").text.strip().replace("CFA", "")
            Adresse=Paquet.find("p", class_="ad__card-location").text.replace("location_on", "")
            Image_lien=Paquet.find("img", class_="ad__card-img")["src"]
            dic= {
                "Type chaussure":Type_chaussures,
                "Prix": Prix,
                "Adresse": Adresse,
                "Image lien":Image_lien,
            }
            data.append(dic)
       except :
              pass
    DF1=pd.DataFrame(data)
    df= pd.concat([df,DF1], axis=0).reset_index(drop=True)

        return df   
                                                            # PARTIE 4
    
    st.sidebar.header("Saisie de l'utilisateur")
    Pages = st.sidebar.selectbox('Pages', list([int(p) for p in np.arange(2, 30)]))
    Category = st.sidebar.selectbox("Options", ["Scrape les données avec beautifulSoup", "Scarper les données avec web Scarper" , "Formulaire avec koblox", "Formulaire avec Google Forms"])
    
    # Fonction pour injecter du CSS personnalisé
    def local_css(css):\
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    
    # CSS personnalisé
    couleur_css = 
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f6;
        }
        h1 {
            color: #4a90e2;
            text-align: center;
          }
        .stButton button {
            background-color: #4a90e2;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #357abd;
        }\
    
    # Appeler la fonction pour appliquer le CSS
    local_css(couleur_css)

    
    if Category=="Scrape les données avec beautifulSoup":
    
        Vetements_enfants = scrape_vetements_data(Pages)
        Chaussures_enfants = scrape_chaussures_data(Pages)
        
        load(Vetements_enfants, "Données sur les vetements", '1', '110')
        load(Chaussures_enfants, "Données sur les chaussures", '2', '111')
    
    elif Choices == "Scarper les données avec web Scarber": 
        Vetements = pd.read_csv("Vetements_enfants.csv")
        Chaussures = pd.read_csv("chaussure_enfants (1).csv") 
    
        load(Vehicles, 'Vehicles data', '1', '110')
        load(Motocycles, 'Motocycles data', '2', '111')
    
    
    
    
    else :
        components.html("""
        <iframe src="https://ee.kobotoolbox.org/x/lWB14KiL" width="800" height="1100"></iframe>,
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScuuEKdEs1FmIeYDq3TrUT2TiNqc1OIT7GPG0hCa2fx52_q_A/viewform?usp=preview"></iframe>
        """,height=1100,width=800)
 
