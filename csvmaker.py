# Written for startups.vet data
#
# 2016 Sep 16   -   Ronald Rihoo
#


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
