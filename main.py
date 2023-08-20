from collections import namedtuple

PHONEBOOK = 'phonebook.txt'
LINE_IN_PAGE = 3
Note = namedtuple('Note', 's_name name p_name org j_phone h_phone')


def show_pages():
    """
    Show pages. One page = 3 lines
    :return:
    """
    with open('phonebook.txt', mode="r", encoding="utf-8") as f:
        while True:
            for _ in range(LINE_IN_PAGE):
                line = f.readline().strip()
                if line:
                    data = Note(*line.split(','))
                    print(f'Фамилия: {data.s_name} |Имя: {data.name} |Отчество: {data.p_name} |Организация: {data.org} '
                          f'|Рабочий Номер: {data.j_phone} |Домашний номер: {data.h_phone}')
                else:
                    print('Записей больше нет')
                    return
            print('Продолжить? Нажмите n для завершения')
            answer = input()
            if answer == 'n':
                return


def add_line(info: Note):
    """
    Add new line with name, organization etc. from info
    :param info: information about person namedtuple Note
    :return:
    """
    with open(PHONEBOOK, mode="a", encoding="utf-8") as f:
        print(f'{info.s_name},{info.name},{info.p_name},{info.org},{info.j_phone},{info.h_phone}', file=f)


def edit_line(old: str, new: str):
    """
    Transform old note to new note
    :param old: str old note in the phonebook
    :param new: str new information
    :return:
    """
    file_new = []
    with open('phonebook.txt', mode="r", encoding="utf-8") as f:
        while True:
            file_old = f.readline()
            if not file_old:
                break
            if file_old != old:
                file_new.append(file_old)
            else:
                file_new.append(new)
    with open('phonebook.txt', mode="w", encoding="utf-8") as f:
        f.writelines(file_new)


def search(info: str):
    """
    Search line with info
    :param info: word for search
    :return:
    """
    with open('phonebook.txt', mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            if info in line:
                data = Note(*line.split(","))
                print(f'Фамилия: {data.s_name} |Имя: {data.name} |Отчество: {data.p_name} |Организация: {data.org} '
                      f'|Рабочий Номер: {data.j_phone} |Домашний номер: {data.h_phone}')


def main():
    """
    Main block that gets data and call another func
    :return:
    """
    while True:
        print("\n1.Вывести записи\n2.Добавить запись\n3.Отредактировать запись\n4.Найти запись\n5.Выйти")
        option = input()
        if option == '1':
            show_pages()
        elif option == '2':
            info = Note(input('Введите фамилию: '), input('Введите имя: '), input('Введите отчество: '),
                        input('Введите организацию: '), input('Введите рабочий номер: '),
                        input('Введите домашний номер: '))
            add_line(info)
        elif option == '3':
            print("Вводите старую информацию")
            old = f"{input('Введите фамилию: ')},{input('Введите имя: ')},{input('Введите отчество: ')}," \
                  f"{input('Введите организацию: ')},{input('Введите рабочий номер: ')}," \
                  f"{input('Введите домашний номер: ')}\n"
            print("Вводите новую информацию")
            new = f"{input('Введите фамилию: ')},{input('Введите имя: ')},{input('Введите отчество: ')}," \
                  f"{input('Введите организацию: ')},{input('Введите рабочий номер: ')}," \
                  f"{input('Введите домашний номер: ')}\n"
            edit_line(old, new)
        elif option == '4':
            info = input('Введите информацию для поиска: ')
            print("Результаты поиска:")
            search(info)
        elif option == '5':
            break
        else:
            print('Неизвестная команда')


if __name__ == '__main__':
    main()
