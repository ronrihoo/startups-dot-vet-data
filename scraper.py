# scraper.py
#
# In its early stages, so the name doesn't entirely fit.
#
# 2016 Oct 01   -   Ronald Rihoo
#

import urllib.request


class Scraper:

    def __init__(self):
        pass

    def read_remote_html_file(self, remote_address):

        """
        reads HTML code from a remote HTML file over the internet

        ; param remote_address: URL to an html file
        ; return: a string of the HTML code
        """

        sock = urllib.request.urlopen(self, remote_address)
        string = sock.read()
        sock.close()
        return string

    def read_local_html_file(self, path):

        """
        reads HTML code from an HTML file stored on the local storage

        ; param path: path to an html file
        ; return: a string of the HTML code
        """

        import codecs
        return codecs.open(path, 'r').read()
