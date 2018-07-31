# API - Campeonato Brasileiro Série A
import requests
from bs4 import BeautifulSoup

data = []
clubs = []

request = requests.get('https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a')
soup = BeautifulSoup(request.text, 'html.parser')
info = soup.find_all('tr', class_="expand-trigger")

for td in info:
    data.append(td.get_text()[3:-12].strip())

for r_spaces in data:
    clubs.append(r_spaces.split('\n'))

print('_' * 94)
print(f'\033[32m\n{" Campeonato Brasileiro Série A ":^94}\033[m')
print('_' * 94, '\n')
print(f'\033[33mClassificação                              P    J    V   E   D   GP   GC    SG   CA   CV   %\033[m\n')

for club in clubs:
    if club in clubs[0:4]:
        print(f'{club[0]:>3}  {club[1]:>2}  \033[36m{club[3]:<19}\033[m\t\t  {club[5]:>2}   {club[6]:>2}   {club[7]:>2}'
              f'  {club[8]:>2}  {club[9]:>2}   {club[10]:>2}   {club[11]:>2}   {club[12]:>3}   {club[13]:>2}'
              f'   {club[14]:>2}   {club[15]:>2}')
    elif club in clubs[4:16]:
        print(f'{club[0]:>3}  {club[1]:>2}  {club[3]:<19}\t\t  {club[5]:>2}   {club[6]:>2}   {club[7]:>2}'
              f'  {club[8]:>2}  {club[9]:>2}   {club[10]:>2}   {club[11]:>2}   {club[12]:>3}   {club[13]:>2}'
              f'   {club[14]:>2}   {club[15]:>2}')
    elif club in clubs[16:20]:
        print(f'{club[0]:>3}  {club[1]:>2}  \033[31m{club[3]:<19}\033[m\t\t  {club[5]:>2}   {club[6]:>2}   {club[7]:>2}'
              f'  {club[8]:>2}  {club[9]:>2}   {club[10]:>2}   {club[11]:>2}   {club[12]:>3}   {club[13]:>2}'
              f'   {club[14]:>2}   {club[15]:>2}')
                                                        
print('_' * 94, '\n')
print(f'\nB\'H\'A - Bendito seja o Pai que está nos céus!\n\nJonh Santos\n')
print('_' * 94, '\n')