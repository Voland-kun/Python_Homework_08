def manual_input(mode):
    if mode == '1':
        last_name, phone_number, comment = input(
            'Введите фамилию, номер телефона и комментарий через пробел: ').split(maxsplit=2)
        res_line = '; '.join([last_name, phone_number, comment])
        return res_line
        
    if mode == '2':
        last_name = input('Введите фамилию: ')
        phone_number = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        res_line = '; '.join([last_name, phone_number, comment])
        return res_line

def output_variants(mode, txt):
    while mode not in '12':
            print('Вы ввели некорректное значение')
            mode = input('Выберите формат вывода информации: 1. В одну строку 2. В несколько строк ')
    if mode == '1':
        temp_txt = txt.split('\n')
        for line in temp_txt:
            i = line.split('; ')
            print('; '.join(i))
    if mode == '2':
        temp_txt = txt.split('\n')
        for line in temp_txt:
            i = line.split('; ')
            print('\n'.join(i))
            print()

            

    #       if mode == '1':
    #           for i in txt:
    #               print('; '.join(i))
    #       if mode == '2':
    #           for i in txt:
    #               print('\n'.join(i))
    #               print()



# if mode == '1':
#         temp_txt = txt.split('\n')
#         for line in temp_txt:
#             i = line.split('; ')
#             for i in line:
#                 print('; '.join(i))