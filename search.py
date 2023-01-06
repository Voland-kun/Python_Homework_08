def surename_search(surename):

    with open('book.csv', 'r') as data:
        result = ''
        #lines_list = data.read().split('\n')
        temp_search = data.read()
        #print(temp_search)
        #for line in temp_search:
        temp_list = temp_search.split('\n')
        #print(temp_list)
        for line in temp_list:
            li = line.split('; ')
            print(li)

            if li[0].lower() == surename.lower():
                result += '; '.join(temp_list) + '\n'
        if result == '':
            print('Совпадений не обнаружено')
    return result

