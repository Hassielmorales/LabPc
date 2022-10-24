from bs4 import BeautifulSoup
import requests

url = 'https://mexico.as.com/resultados/futbol/mexico_apertura/clasificacion/'

pag = requests.get(url)

soup=BeautifulSoup (pag.content, 'html.parser')

#Posiciones de equipos liga mx

pos = soup.find_all('span', class_='nombre-equipo')

equipos = list()

for i in pos:
    equipos.append(i.text)

print(equipos)


with open('Posiciones.txt','w') as f:
    f.write(str(equipos))
