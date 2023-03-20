from bs4 import BeautifulSoup
import requests
import os
from pars_number import list_of_values



BASE_DIR = "F:/python/ПАРСЕР_САНТЕХ/"

headers = { # Это что-то вроде маски под которой мой комп заходит на сайты, чтобы его не забанили, т.к. без него может быть такая возможность
    "Accept":"*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    } 



if __name__ == '__main__':
    
    folder_for_all_documents = os.path.join(BASE_DIR, 'folder')
    os.mkdir(folder_for_all_documents)

    for item in list_of_values:  
        
        # Через поиск находим нужный нам адрес и пихаем его в get_to_product

        server = "https://www.santech.ru"
        resp = requests.get("https://www.santech.ru/catalog/autocomplete/?term=%s" % item) # Тут получаю через поисковую строку адрес нужного мне товара
        soup = BeautifulSoup(resp.text, "lxml")
        
        #  Проверяем есть ли ссылка, т.к. может быть такое что товар есть в моём списке, но его нет на нужном сайте
        alert_block = soup.find(class_="ss-p-10")
        if alert_block is not None:
            continue

        # Тут забираю нужную мне ссылку и присваиваю её get_to_product
        product_url = soup.find(class_="ss-search-item").find("a")
        get_to_product = product_url["href"]

        # Заходим на страницу с нужными данными
        req = requests.get(server + get_to_product, headers=headers) 
        # Забираем это как текст
        new_site = BeautifulSoup(req.text, "lxml") 

        #  Здесь запишем название Товара
        title = new_site.find(class_="product__title")


        # Здесь запишем нужные нам страницы в html файлы, чтобы больше не посылать запросы к сайту
        with open(f"{folder_for_all_documents}/{item}.html", "w", encoding="utf-8") as file:
            file.write(req.text)