import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www.nike.com.br/nav/esportes/casual/genero/masculino/idade/adulto/tipodeproduto/calcados?page=2'

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
    }

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

dic_produtos = {'nome':[], 'preco':[]}
produtos = soup.find_all('div', class_=re.compile('ProductCardContainer'))
paginas = 1

for i in range(1, paginas+1):
        url = f'https://www.nike.com.br/nav/esportes/casual/genero/masculino/idade/adulto/tipodeproduto/calcados?page={i+1}'
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
       
        for produto in produtos:
                nome = produto.find('p', class_=re.compile('Styled')).get_text().strip()
                tipo = produto.find('p', class_=re.compile('Typography')).find_next('p').get_text().strip()
                preco = produto.find('p', class_=re.compile('Typography')).find_next('p').find_next('p').get_text().strip()
                print(nome,'(',tipo,')',preco)
