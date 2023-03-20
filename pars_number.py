# Функция для того чтобы забрать из эксель файла номенклатурные номера которые мне нужны для поиска

import os
import pandas as pd


def is_number(str): # Думаю тут понятно что за функция
    try:
        float(str)
        return True
    except ValueError:
        return False


def find_file(find): # Тут этой функцией я нахожу файл который мне нужен на моём диске 
    dir = "C:/Users/skyfi/Desktop/DN/клапаны запорные"
    list_of_files = []

    for root, dirs, files in os.walk(dir):
        
        list_of_files.append([_ for _ in files])
    

    for a in list_of_files:
        for g in a:
            if find in g:
                return dir +"/" + g


dict_ = pd.read_excel(find_file("Ронжина"), index_col=0) # Тут считываю в переменную файл

new_dict = dict_.to_dict() # Делаю из этой переменной словарь
new_dict_values = new_dict.values() # Забираю только значения, хз зачем, дальше не смотрел
list_of_values = []
test_list = []


for a, c in new_dict.items(): # захожу в значения словаря
    for g,h in c.items(): # тут захожу в значения значений словаря, т.к. там был словарь словарей
        # print(g, h)
        # if type(h) is int and h > 0: # тут отбираю только те радиаторы которые есть в наличии
            # list_of_values.append(g) # добавляю нужные значения в список
        # else:
        list_of_values.append(g)

list_of_values = list(set(list_of_values))




    # for digits in c:
    #     list_of_values.append(digits)
        # if digits.isalpha() is not True:
        #     list_of_values.append(digits)
    # for b in a.values():
    #     if is_number(b) and b > 0:
    #         print(b)
        

        
