import time
import requests
from bs4 import BeautifulSoup

full_sp = []
company = []

#Счетчик времени выполнения кода
start_time = time.time()

#Данные о компаниях
igroconsole = ['https://igroconsole.ru/keys?sort=pd.name&order=ASC&ocf=F4S0V1&page=', '5', 'span', 'price-new', 'div', 'caption']
xboxstor = ['https://xboxstor.ru/katalog-xbox/?page=', '8', 'p', 'price', 'div', 'caption']

#Выбор компании
print('По какой компании нужны данные?', '1) igroconsole.ru', '2) xboxstor.ru')
choice = input('Введите номер компании: ')
print('Загрузка...')

if int(choice) == 1:
    company = igroconsole
elif int(choice) == 2:
    company = xboxstor

for page in range(1, int(company[1])):
    #Получение html кода сайта
    url = str(company[0]) + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    #Получение названия и стоимости игры
    prices_tag = soup.find_all(str(company[2]), class_=str(company[3]))
    names_tag = soup.find_all(str(company[4]), class_=str(company[5]))

    #сохранение данных о ценах в список price_sp
    if int(choice) == 1:
        prices_sp = []
        for price in prices_tag:
            prices_sp.append(price.text)
    elif int(choice) == 2:
        prices_sp = []
        for price in prices_tag:
            prices_sp.append((price.text).strip())

    #сохранение данных о названиях в список names_sp
    if int(choice) == 1:
        old_names_sp = []
        for names in names_tag:
            old_names_sp.append(names.text)
        names_sp = []
        for i in old_names_sp:
            start_index = 1
            end_index = i.find("(")
            new_i = i[start_index:end_index]
            names_sp.append(new_i)
    elif int(choice) == 2:
        old_names_sp = []
        for names in names_tag:
            old_names_sp.append(names.text)
        names_sp = []
        for i in old_names_sp:
            new_i = i[1:]
            names_sp.append(new_i[0:new_i.find('\n')])

    #список с ценами и названием
    for i in range(len(names_sp)):
        full_sp.append((names_sp[i], prices_sp[i]))

#вывод списка
print('Список игр компании:')
for i in full_sp:
    print(i)

end_time = time.time()
print('')
print('Время выполнения программы:', round(end_time - start_time, 2), 'сек.')