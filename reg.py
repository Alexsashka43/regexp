from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


#### функция 1 #### открываем файл
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


#### функция 2 #### Создаем лист с информацией
info_in_list = ''
for i in contacts_list:
    info_in_list += '\n'
    for list in i:
        info_in_list += (list + ',')
persons = re.compile('(\,)*')
result = re.sub(persons, r'\1', info_in_list)
persons = re.compile('([А-Я][а-я]+)\s*\,*([А-Я][а-я]+)\s*\,*')
result = re.sub(persons, r'\1,\2,', result)
persons = re.compile('(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})')
result = re.sub(persons, r'+7(\2)\3-\4-\5', result)
persons = re.compile('\s*\(*(доб.)\s*(\d+)\)*\s*')
result = re.sub(persons, r' \1\2', result)
list = result.split('\n')
list.pop(0)
list_number = []


#### функция 3 #### редактируем информацию 
for i in list:
    info_in_list = (i.split(','))
    info_in_list.remove('')
    list_number.append(info_in_list)
for i in list_number:
    for info_in_list in list_number:
        try:
            if i[0] == info_in_list[0]:
                if i != info_in_list:
                    for num in range(1,10):
                        for z in i:
                            if z in info_in_list:
                                i.remove(z)
                            else:
                                info_in_list.append(z)
                                i.remove(z)
        except:
            pass
text = ''
for i in list_number:
     if len(i) == 0:
          list_number.remove(i)
list_number.sort()


#### функция 4 #### Закрываем файл
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',' )
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(list_number)
