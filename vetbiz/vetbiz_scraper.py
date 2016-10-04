# Brief: scrapes https://www.vip.vetbiz.gov/Public/Search/Default.aspx
#
# Written for startups.vet
#
# 2016 Oct 01   -   Ronald Rihoo
#

import time
import urllib.request

import pathmaker as pathmaker


def modify_url(index=0):
    url = 'https://www.vip.vetbiz.gov/Public/Search/ExportSearchResults.aspx?SCID=3369234&PageIndex=' \
          + str(index) + '&PageSize=100'
    return url


def get_urls(iterations):
    urls = []
    for iteration in range(iterations):
        urls.append(modify_url(iteration))
    return urls


def generate_filenames(quantity):
    filenames = []
    for number in range(quantity):
        filenames.append('vip.vetbiz.gov.set' + str(number + 1) + '.xls')
    return filenames


def download_files(links, filenames):
    for index, link in enumerate(links):
        print("Downloading " + filenames[index] + " from " + link)
        try:
            urllib.request.urlretrieve(link, filenames[index])
        except:
            print("Download failed...")
        time.sleep(2)   # courteous conduct


def run():
    pathmaker.make_path('excel_files')
    links = get_urls(91)
    filenames = generate_filenames(len(links))
    download_files(links, filenames)
    print("All downloads completed.")


# run()
