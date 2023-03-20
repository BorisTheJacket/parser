from bs4 import BeautifulSoup
import json
import os
from pandas import DataFrame


variable_dict = {} # Здесь будет словарь со значениями внутри цикла
pod_zakaz = [] # Список словарей, нужен чтобы работать с dataframe, так как он таким образом засовывает в эксельку
list_of_dict = []

headers = { # Это что-то вроде маски под которой мой комп заходит на сайты, чтобы его не забанили, т.к. без него может быть такая возможность
    "Accept":"*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    } 

if __name__ == '__main__':


    for item in os.listdir("F:/python/ПАРСЕР_САНТЕХ/folder/"): # Захожу папку с хтмлками

        file_path = f'F:/python/ПАРСЕР_САНТЕХ/folder/{item}'
            
        with open(file_path, encoding="utf-8") as f:
            new_site = BeautifulSoup(f, "html.parser") 
            # Тут вызываю бютифул суп чтобы мочь парсить
            
            new_table_name = []
            table_value = []
            
            print(item)
            
            title = new_site.find(class_="product__title").text.strip() 
            # Тут Забираю название Товара

            if new_site.find(class_='territory-choose__list-count').text.strip() == "под заказ":
                
                for element in new_site.find_all(class_="property__table-tr"):
                    if element.find(class_="property__table-name") is not None:
                        if element.find(class_="title") is not None:
                            new_table_name.append(element.find(class_="title").text.strip())
                        else:
                            new_table_name.append(element.find(class_="property__table-name").text.strip())
                        table_value.append(element.find(class_="property__table-value").text.strip())
                        
                    elif element.find(class_="title") is not None:
                        new_table_name.append(element.find(class_="title").text.strip())
                        table_value.append(element.find(class_="property__table-value").text.strip())
                        
                    else:
                        new_table_name.append(element.find(class_="property__table-name item-specs-col").text.strip())
                        table_value.append(element.find(class_="property__table-value item-specs-col").text.strip())
                        

            #     # Тут забираю все значения из таблицы

            
                variable_dict = {new_table_name[i]: table_value[i] for i in range(0, len(new_table_name))} # Делаю словарь из двух списков
                variable_dict['Название'] = title # Добавляю в словарь название Товара
                
                pod_zakaz.append(variable_dict) # Добавляю словарь в список, чтобы мочь его вывести в эксельку
            else:
                for element in new_site.find_all(class_="property__table-tr"):
                    if element.find(class_="property__table-name") is not None:
                        if element.find(class_="title") is not None:
                            new_table_name.append(element.find(class_="title").text.strip())
                        else:
                            new_table_name.append(element.find(class_="property__table-name").text.strip())
                        table_value.append(element.find(class_="property__table-value").text.strip())
                        
                    elif element.find(class_="title") is not None:
                        new_table_name.append(element.find(class_="title").text.strip())
                        table_value.append(element.find(class_="property__table-value").text.strip())
                        
                    else:
                        new_table_name.append(element.find(class_="property__table-name item-specs-col").text.strip())
                        table_value.append(element.find(class_="property__table-value item-specs-col").text.strip())
                        

                # Тут забираю все значения из таблицы

            
                variable_dict = {new_table_name[i]: table_value[i] for i in range(0, len(new_table_name))} # Делаю словарь из двух списков
                variable_dict['Название'] = title # Добавляю в словарь название Товара
                
                list_of_dict.append(variable_dict) # Добавляю словарь в список, чтобы мочь его вывести в эксельку

            
    
    with open(f"{' '.join(pod_zakaz[0]['Название'].split()[:3])} под заказ.json", "w", encoding="utf-8") as f:
        json.dump(pod_zakaz, f, ensure_ascii=False, indent=4)


    df = DataFrame(sorted(pod_zakaz, key=len)) # Собственно выхываю датафрейм к этому списку и засовываю его в эксельку
    df.to_excel(f"{' '.join(pod_zakaz[0]['Название'].split()[:3])} под заказ.xlsx", sheet_name="sheet2", index=False)
    
    with open(f"{' '.join(list_of_dict[0]['Название'].split()[:3])} в наличии.json", "w", encoding="utf-8") as f:
        json.dump(list_of_dict, f, ensure_ascii=False, indent=4)


    df = DataFrame(sorted(list_of_dict, key=len)) # Собственно выхываю датафрейм к этому списку и засовываю его в эксельку
    df.to_excel(f"{' '.join(list_of_dict[0]['Название'].split()[:3])} в наличии.xlsx", sheet_name="sheet2", index=False)

        
        