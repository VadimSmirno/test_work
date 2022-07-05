import requests
from bs4 import BeautifulSoup

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
dct = {letter : 0 for letter in alphabet }

url = 'https://inlnk.ru/jElywR'
html = requests.get(url= url).text
while True:
    flag = False
    soup = BeautifulSoup(html, 'lxml')
    url2 = soup.find('div',id='mw-pages').find(text='Следующая страница').parent.get('href')
    next_page= f'https://ru.wikipedia.org/{url2}'
    result = soup.find('div', class_='mw-category mw-category-columns').find('div', class_='mw-category-group').find('ul').find_all('li')


    for i in result:
        dct[i.text[0]] += 1
        if i.text == 'Ящурки':
            flag = True
    if flag:
        break
    html = requests.get(url=next_page).text
for key,value in dct.items():
    print(f'{key} : {value}')