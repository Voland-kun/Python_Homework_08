from search import surename_search
from inout import *
from file_import import *

def mode():
    mode_m = input('Выберите режим работы\n'
                '1) Режим ручного внесения записей\n'
                '2) Режим просмотра записей\n'
                '3) Режим поиска по фамилии\n'
                '4) Импорт из файла\n')

    if mode_m == '1':
        print('Выбран режим внесения записей\n')
        mode = input('Выберите формат ввода данных: 1) В одну строку 2) В несколько строк\n')
        add_strings(manual_input(mode))
    elif mode_m == '2':
        mode = input('Выбран режим просмотра записей\n'
                    'Выберите вид записей\n'
                    '1) Показать записи одной строкой\n'
                    '2) Показать записи в столбик\n')
        with open('book.csv', 'r') as data:
            show_book = data.read()
            output_variants(mode, show_book)
    elif mode_m == '3':
        print('Выбран режим поиска по фамилии')
        surename = input('Введите  фамилию для поиска: \n')
        search_res = surename_search(surename)
        if search_res != '':
            mode = input('Выберите формат ввода данных: 1) В одну строку 2) В несколько строк\n')
            output_variants(mode, search_res)
        else:
            pass
    elif mode_m == '4':
        import_file = input('Введите имя файла из которого будет импорт\n')
        mode = input('Выберите формат содержащихся в файле данных: 1) В одну строку 2) В несколько строк\n')
        if mode == '1':
            with open(str(import_file), 'r') as input_data:
                txt = input_data.read()
                add_strings(txt)
        elif mode == '2':
            add_strings(import_row(import_file))

mode()