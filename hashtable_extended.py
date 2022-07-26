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
            return (i['name'])

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
        print('№: ' + str(i['type']) + ', тип: ' + type + ', владелец: ' + str(i['name']) +
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


def adddock(number, type, owner, shelf):
    new = {'type': type, 'number': number, 'name': owner}
    documents.append(new)
    print(documents)
    directories[shelf] = list([number])
    print(directories)
    print("Документ добавлен. Текущий список документов: ")
    for i in documents:
        numb = str(i['number'])

        key = [k for k, v in directories.items() for i in v if i == numb][0]
        print('№: ' + numb + ', тип: ' + str(i['type']) + ', владелец: ' + str(i['name']) +
              ', полка хранения: ' + key)


def delldock(n):
    flag = False
    for i in range(len(documents)):
        if documents[i]['number'] == n:
            del documents[i]
            flag = True
            break

    if flag == False:
        print("Документ не найден в базе.")
        print("Текущий список документов:")
        for i in documents:
            numb = str(i['number'])

            key = [k for k, v in directories.items() for i in v if i == numb][0]
            print('№: ' + numb + ', тип: ' + str(i['type']) + ', владелец: ' + i['name'] +
                  ', полка хранения: ' + key)

    else:
        print("Документ удален.")
        print("Текущий списко документов: ")
        for i in documents:
            numb = str(i['number'])

            key = [k for k, v in directories.items() for i in v if i == numb][0]
            print('№: ' + numb + ', тип: ' + str(i['type']) + ', владелец: ' + i['name'] +
                                                  ', полка хранения: ' + key)


def swap(number, shelfer):
    #for shelfer in d
    flag = False
    flagg = True
    arr = list(directories.keys())
    for key, value in directories.items():
        for j in value:
            if j == number:
                directories[shelfer] = directories[key]
    if not shelfer in arr:
        flagg == False
        per = offor()
        print("Такой полки не существует. Текущий перечень полок: " + per)
    else:
        for i in range(len(documents)):
            if documents[i]['number'] == number:
                flag = True
                break

        if flag == False:
            print("Документ не найден в базе.")
            print("Текущий список документов:")
            for i in documents:
                numb = str(i['number'])

                key = [k for k, v in directories.items() for i in v if i == numb][0]
                print('№: ' + numb + ', тип: ' + str(i['type']) + ', владелец: ' + i['name'] +
                      ', полка хранения: ' + key)

        else:
            print(documents)
            print(directories)
            print("Документ перемещен.")
            print("Текущий список документов:")
            for i in documents:
                numb = str(i['number'])

                key = [k for k, v in directories.items() for i in v if i == numb][0]
                if numb == number:
                    key = shelfer
                print('№: ' + numb + ', тип: ' + str(i['type']) + ', владелец: ' + i['name'] +
                      ', полка хранения: ' + key)


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

    if item == 'ad':
        print('Введите номер документа:')
        n = input()
        print('Введите тип документа:')
        t = input()
        print('Введите владельца документа:')
        o = input()
        print('Введите полку для хранения:')
        s = input()
        adddock(n, t, o, s)

    if item == 'd':
        print('Введите номер документа:')
        n = input()
        delldock(n)

    if item == 'm':
        print('Введите номер документа:')
        n = input()
        print('Введите номер полки:')
        s = input()
        swap(n, s)

choice()


