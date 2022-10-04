import texttable    # ввести в терминал pip install texttable
import codecs
import re


def sort_str(data):
    sample_data = data.readlines()
    sample_data.sort()
    arr = []

    for i in range(len(sample_data)):
        arr.append(sample_data[i])

    remove_n = []
    for sub in arr:
        remove_n.append(re.sub('\n', '', sub))

    cleared = []
    for sub in remove_n:
        cleared.append(re.sub('\r', '', sub))

    return cleared


def formating(data, value):
    i = 0
    lst_f = []
    for i in range(len(data)):
        lst = list(data[i].split(' '))
        lst.insert(4, value)
        temp = lst[5]
        lst.pop(5)
        lst.insert(7, temp)
        fio = " ".join(lst[0:3])
        del lst[0:3]
        lst.insert(0, fio)
        lst_f.append(lst)
    return lst_f


table = texttable.Texttable()
app_inf = codecs.open('AI_students.txt', 'r', 'utf-8')
inf_sec = codecs.open('IS_students.txt', 'r', 'utf-8')

app_inf_list = sort_str(app_inf)
inf_sec_list = sort_str(inf_sec)

final_app = formating(app_inf_list, 'Прикладная информатика')
final_inf = formating(inf_sec_list, 'Защита информации')
table.set_cols_align(['l', 'c', 'l', 'c', 'c', 'c', 'c'])
table.set_cols_dtype(['t', 't', 't', 't', 't', 't', 't'])
table.add_rows([['Фамилия Имя Отчество', 'Дата рождения', 'Специальность', 'Курс', 'Группа', 'Балл при поступлении',
                 'Срредний Балл']],
               header=True)
for i in range(len(final_app)):
    table.add_row(final_app[i])
for i in range(len(final_inf)):
    table.add_row(final_inf[i])

print(table.draw())



