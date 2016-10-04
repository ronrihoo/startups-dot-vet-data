# Written for startups.vet data
#
# 2016 Sep 16   -   Ronald Rihoo
#


def xls_to_csv(data):
    csv_data = []
    for row in data:
        for index, cell in enumerate(row):
            try:
                if ',' in cell:
                    if type(cell) == type(u''):
                        cell = cell.encode('utf-8')
                    csv_data.append('\"{}\"'.format(cell))
                else:
                    csv_data.append('{}'.format(cell))
            except:
                csv_data.append('{}'.format(cell))
            if index != len(row) - 1:
                csv_data.append(','.format(cell))
        csv_data.append('\n')
    return hotfix_for_xls_to_csv(''.join(csv_data))


def hotfix_for_xls_to_csv(csv_data):
    return csv_data.replace('b"', 'b\'').replace('b\'', '').replace('""', '"').replace('\'"', '"').replace('\t', '')


def convert_to_csv(data):
    csv_data = []
    for items in data:
        for index, dictionary in enumerate(items):
            if index == 0:
                string = '{}'
            else:
                string = ',{}'
            for key in dictionary:
                csv_data.append(string.format(key).replace(':', ''))
        csv_data.append('\n')
        break
    for items in data:
        for index, dictionary in enumerate(items):
            if index == 0:
                string = '{}'
            else:
                string = ',{}'
            for key in dictionary:
                csv_data.append(string.format(dictionary[key]).replace(':', ''))
        csv_data.append('\n')
    return ''.join(csv_data)


def save_conversion_to_file(filename, data):
    if '.csv' not in filename:
        filename += '.csv'
    with open(filename, 'w') as target:
        target.write(data + '\n')


def print_conversion_to_screen(data):
    print(convert_to_csv(data))
