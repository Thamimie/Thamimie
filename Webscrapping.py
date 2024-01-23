#importation de quelques modules
import requests
from bs4 import BeautifulSoup
import csv

#Lien cible
link = 'https://lenouvelliste.com/'

# Obtenir la reponse HTTP
response = requests.get(link) 

#Verifier si la requete a reussi (code d'etat 200)
if response.ok:
    supp = BeautifulSoup(response.text, "html.parser") #Instance de BeautifulSoup
    tit = supp.find_all('h1') #Extraction du titre de chaque l'article
    lyen = supp.find_all('a')#Extraction des liens
    atik_lis = supp.find_all('div', class_= 'lnv-featured-article-lg' )

    # print(len(tit))
    # print(len(lyen))
    # print(len(atik))

    data = []
    lyen_imaj =[]
    for lis in atik_lis :
        imaj_tag = lis.find('img')
        if imaj_tag :
            sous = imaj_tag.get ('scr')
            data.append([tit, lyen, atik_lis, sous])
       
#stocker les donnees dans un fichier csv
with open('Done.csv', mode = 'w', newline= '') as file :
    writer = csv.writer(file)

    writer.writerow(['Titres'])  
    for a in tit:
        writer.writerow([a.text.strip()])  
            
        writer.writerow(['Liens'])
        for b in lyen : 
              writer.writerow([b.text.strip()])
    
        writer.writerow(['Lien des Images ']) 
        for c in lyen_imaj:
            writer.writerow([link])

for d in data:
    print(data)
    

