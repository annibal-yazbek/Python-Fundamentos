""" Exemplo de Webscraping 
    - Extraindo dados de uma página web usando BeautifulSoup e requests
    Objetivo: Listar os Episódios de Game of Thrones, diretores, autores, 
    data de lançamento e público . Usando como referência uma página da
    Wikipedia."""

import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
r = requests.get(url)
html_content = r.text
html_soup = BeautifulSoup(html_content, 'html.parser')
#
episodes = []
ep_tables = html_soup.find_all('table', class_='wikiepisodetable')
for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    #
    # 
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)

    for row in table.find_all('tr')[1:]:
        values = []
        #
        for col in row.find_all(['th', 'td']):
            values.append(col.text)
        if values:
            episode_dict = {headers[i]: values[i] for i in
            range(len(values))}
            episodes.append(episode_dict)
            
for episode in episodes:
    print(episode)

