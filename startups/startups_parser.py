# Brief: scrapes http://www.startups.vet/companies
#
# Written for startups.vet
#
# 2016 Sep 16   -   Ronald Rihoo
#

import urllib.request
from bs4 import BeautifulSoup
import pathmaker
import csvmaker


# reads HTML code from a remote HTML file over the internet
# returns a string of the HTML code
def read_remote_html_file(remote_address):
    sock = urllib.request.urlopen(remote_address)
    string = sock.read()
    sock.close()
    return string


# reads HTML code from an HTML file stored on the local storage
# returns a string of the HTML code
def read_local_html_file(directory):
    import codecs
    return codecs.open(directory, 'r').read()


def apply_hard_fixes(category):
    # hard-fix: " Website" -> "Website"
    if category[0][0] == ' ':
        category[0] = category[0].replace(' ', '')

    # hard-fix: " Employees" -> "Employees"
    if category[1][0] == ' ':
        category[1] = category[1].replace(' ', '')

    return category


def parse_data(html):
    data = BeautifulSoup(html, 'html.parser')

    categories = data.find_all('div', {'class': 'listsubheading company-attribute'}, limit=9)
    values = data.find_all('div', {'class': 'listsubheadingopp'}, limit=9)

    category = []
    value = []

    for item in categories:
        category.append(item.getText())

    category = apply_hard_fixes(category)

    for item in values:
        value.append(item.getText())

    return category, value


def get_company(page_url, local=False):
    data = []

    if local:
        html = read_local_html_file(page_url)
    else:
        html = read_remote_html_file(page_url)

    category, value = parse_data(html)

    for index, value in enumerate(value):
        # string values, where commas can be placed -- creates difficulties in producing .csv file
        if index == 0 or index == 3 or index == 5:
            data.append({category[index]: "\"{}\"".format(value)})
        else:
            data.append({category[index]: value})

    return data


def find_links(html):
    link_list = []

    links = BeautifulSoup(html, 'html.parser').find_all('a')

    if links:
        for link in links:
            if '/companies/' in link['href'] and '/new' not in link['href']:
                link_list.append("http://www.startups.vet" + link['href'])

    return link_list


def run(page_url, local=False, path='../csv_files', filename='startups_data'):
    companies = []
    print('Converting HTML data to CSV...')
    if local:
        html = read_local_html_file(page_url)
    else:
        html = read_remote_html_file(page_url)
    links = find_links(html)
    for link in links:
        companies.append(get_company(link, local=False))
    pathmaker.make_path(path)
    print('Creating ' + filename + '.csv...')
    csvmaker.save_conversion_to_file(filename, csvmaker.convert_to_csv(companies))
    print('Conversion is complete.')


run('http://www.startups.vet/companies', local=False)
