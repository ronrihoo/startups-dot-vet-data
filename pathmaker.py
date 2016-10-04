# Brief: makes an arbitrarily named path and changes the current directory to it
#
# Borrowed from findnpeek.py (github.com/ronrihoo/findnpeek) and modified for Python 3
#
# 2016 Oct 01   -   Ronald Rihoo
#

import os


def make_path(pathname):
    loop = 1

    # Allow user to change the folder name
    # pathname = raw_input('Folder name (for this run): ')
    # if (pathname == ''):
    #       pathname = 'findnpeek'

    if '..' in pathname:
        pathname = return_to_parent_dir(pathname)

    fullpath = os.path.realpath(0) + '\\' + pathname

    while loop <= 5:
        print("Looking for " + fullpath)

        if not os.path.isdir(pathname):  # if pathname does not exist
            print("Directory does not exist.")  # notify user
            print("Attempting to make directory " + pathname)
            os.makedirs(pathname)  # make directory using desired pathname
            print("Directory has been made.")
            print("Changing directory to " + pathname)
            os.chdir(pathname)  # change to directory
            print("\\" + pathname + " has been successfully created.")
            loop = 6
        else:  # or else just change directory to it
            print("...\nIt exists.")
            print("Changing directory to /" + pathname)
            os.chdir(pathname)

            if os.getcwd() != fullpath:
                print("Something went wrong. [Trial %d]" % loop)
                loop += 1
            else:
                loop = 6
    return


def return_to_parent_dir(pathname):
    os.chdir('..')
    pathname = pathname[3:]
    if pathname[:3] == '../':
        pathname = pathname[3:]
        pathname = return_to_parent_dir(pathname)
    return pathname
