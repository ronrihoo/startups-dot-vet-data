# Brief: takes vetbiz.gov .xls files and reshapes desired parts into Python lists
#
# Written for startups.vet data
#
# 2016 Oct 02   -   Ronald Rihoo
#

import xlrd
import pathmaker
import csvmaker
from vetbiz.vetbiz_scraper import generate_filenames


def open_xls(path):
    return xlrd.open_workbook(path)


def get_first_sheet(file):
    return file.sheet_by_index(0)


def get_columns(sheet):
    return sheet.row_values(6)


def get_all_rows(data, sheet):
    rows = list(range(7, sheet.nrows))  # first 6 rows do not include core data; row 7 is for columns
    for row in rows:
        data.append(sheet.row_values(row))
    return data


def run(file_quantity, xls_path='./excel_files/', csv_path='../csv_files', csv_filename='vetbiz_data'):
    data = []
    print('Converting XLS files to CSV...')
    # open first .xls file
    file = open_xls(xls_path + 'vip.vetbiz.gov.set1.xls')
    # get sheet
    sheet = get_first_sheet(file)
    # get columns
    data.append(get_columns(sheet))
    # generate filenames for all .xls files
    filenames = generate_filenames(file_quantity)
    # grab rows from all .xls files
    for filename in filenames:
        file = open_xls(xls_path + filename)
        sheet = get_first_sheet(file)
        data = get_all_rows(data, sheet)
    pathmaker.make_path(csv_path)
    print('Creating ' + csv_filename + '.csv...')
    csvmaker.save_conversion_to_file(csv_filename, csvmaker.xls_to_csv(data))
    print("Conversion is complete.")


run(91)
