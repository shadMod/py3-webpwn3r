#!/usr/bin/env python3
"""
# WebPwn3r is a Web Applications Security Scanner
# Author: Ebrahim Hegazy // ShadMod
"""

from urllib.request import urlopen, FancyURLopener

from .costants import (
    HTTPHEADER_SERVER,
    get_green,
    get_bold,
    get_red,
    get_end,
)


class UserAgent(FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"


useragent = UserAgent()


def headers_reader(url):
    # This function will print the server headers such as WebServer OS & Version
    print(get_bold + " \n [!] Fingerprinting the backend Technologies." + get_end)

    # init opener
    url_data = urlopen(url)
    # check url_data status
    if url_data.code == 200:
        print(get_green + " [!] Status code: 200 OK" + get_end)
    if url_data.code == 404:
        print(get_red + " [!] Page was not found! Please check the URL \n" + get_end)
        exit()

    server_ = url_data.headers.get(HTTPHEADER_SERVER)
    # get host_
    host_ = url.split("/")[2]
    print(get_green + " [!] Host: " + str(host_) + get_end)
    print(get_green + " [!] WebServer: " + str(server_) + get_end)

    for _, item in url_data.headers.items():
        for powered in item:
            sig = "x-powered-by"
            if sig in item:
                print(get_green + " [!] " + str(powered).strip() + get_end)
