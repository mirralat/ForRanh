documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}


def offor():
    lst = directories.keys()
    new = str(lst)
    new = new[11:-2]
    newest = new.replace("''", '')
    return newest


def num(n):
    error = 'Документ не найден в базе'
    flag = False
    for i in documents:
        if i['number'] == n:
            flag = True
            return(i['name'])

    if flag == False:
            return error


def shelf(n):
    flag = False
    for i in documents:
        if i['number'] == n:
            flag == True
    for key, value in directories.items():
        for j in value:
            if j == n:
                print("Документ хранится на полке: ", key)
                return 0
    if flag == False:
        print("Документ не найден в базе")

def all():
    for i in documents:
        type = str(i['number'])

        key = [k for k, v in directories.items() for i in v if i == type][0]
        print('№: ' + str(i['type']) + ', тип: ' + type + ', владелец: ' + i['name'] +
             ', полка хранения: ' + key)


def add(n):
    directories[n] = []
    added = offor()
    return added


def remover(n):
    item = directories.items()
    have = offor()
    if directories[n] == []:
        del directories[n]
        deleted = offor()
        print("Такой полки не существует. Текущий перечень полок: " + deleted)
        return 0
    else:
        print("На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: " + have)


def choice():
    print('Введите команду:')
    item = input()
    
    if item == 'p':
        print('Введите номер документа')
        first = input()
        print(num(first))
    
    if item == 's':
        print('Введите номер документа')
        second = input()
        shelf(second)

    if item == 'i':
        all()
    
    if item == 'ads':
        print('Введите номер полки:')
        third = input()
        print('Полка добавлена. Текущий перечень полок: ' + add(third))
    
    if item == 'ds':
        print('Введите номер полки:')
        fourth = input()
        remover(fourth)

choice()

