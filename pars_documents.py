from bs4 import BeautifulSoup
import os
import requests
from pandas import DataFrame as pd
import pandas as pd
import json
from icrawler.builtin import GoogleImageCrawler


list_of_documents = []
server = "https://www.santech.ru"
BASE_DIR = "F:/python/ПАРСЕР_САНТЕХ"

list_of_folders = []
list_of_none = ['"', '/']
list_of_urls = []
list_of_brands = []
filters = dict(
    size='large'
    )



if __name__ == '__main__': # Эта функция нужна для скачивания документов с сайта

    folder_for_all = os.path.join(BASE_DIR, "клапаны запорные")
    folder_for_images = os.path.join(folder_for_all, 'Изображения')
    folder_for_documents = os.path.join(folder_for_all, 'Документы')
    try:
        os.mkdir(folder_for_all)
        os.mkdir(folder_for_images)
        os.mkdir(folder_for_documents)
    except:
        pass

    
    with open('Клапан запорный для в наличии.json', encoding="utf-8") as f:      
        data_dict = json.load(f)     
        for dict in data_dict:    
            if dict['Бренд'] not in list_of_brands:
                google = GoogleImageCrawler(storage={'root_dir': f'{(dict["Название"].replace("/",""))}'})
                google.crawl(keyword=dict['Название'], max_num=2, filters=filters , min_size=(500, 500))
                list_of_brands.append(dict['Бренд'])
            # try:
            #     file_path = f'F:/python/ПАРСЕР_САНТЕХ/folder/{dict["Номенклатурный номер"]}.html'
            #     with open(file_path, encoding='utf-8') as f:
            #         soup = BeautifulSoup(f, 'lxml')
            #         name_of_folder = "".join([_ for _ in dict['Название'] if _ != '.' and _ != '/'])
            #         document = soup.find_all(class_='product__document-link')
            #         folder_of_markirovka = os.path.join(folder_for_documents, name_of_folder)
            #         os.mkdir(folder_of_markirovka) 
            #         for a in document:
            #             document_url = a['href'] # Забираю ссылку на файл
            #             if document_url not in list_of_urls:
            #                 list_of_urls.append(document_url)
                            
            #                 document_name = a.text # Забираю название файла
            #                 path_to_file = os.path.join(folder_of_markirovka, f'{document_name}.pdf')
            #                 response = requests.get(server + document_url) # Тут забираю файл
            #                 with open(path_to_file, "wb") as f: # Тут пихаю в пдфку
            #                     f.write(response.content) # Ещё не проверил, т.к. ещё не изучил как папки создавать
            #             # и туда заходить
            # except:
                
            #     pass
                
    # for path, directory, file in os.walk(folder_for_documents):
    #     if path != folder_for_documents and len(file) == 0:
    #         os.rmdir(path)
            

                
            
