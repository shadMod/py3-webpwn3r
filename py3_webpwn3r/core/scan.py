#!/usr/bin/env python3
"""
# WebPwn3r is a Web Applications Security Scanner
# Author: Ebrahim Hegazy // ShadMod
"""

from costants import (
    get_green,
    get_bold,
    get_red,
    get_end,
)
from vulnz import (
    rce_func,
    xss_func,
    error_based_sqli_func,
)

copyr = """
     __          __  _     _____                 ____       
     \ \        / / | |   |  __ \               |___ \      
      \ \  /\  / /__| |__ | |__) |_      ___ __   __) |_ __ 
       \ \/  \/ / _ \ '_ \|  ___/\ \ /\ / / '_ \ |__ <| '__|
        \  /\  /  __/ |_) | |     \ V  V /| | | |___) | |   
         \/  \/ \___|_.__/|_|      \_/\_/ |_| |_|____/|_|   

################################################################
#| "WebPwn3r" Web Applications Security Scanner               |#
#|  By Ebrahim Hegazy - @Zigoo0 - ShadMod                     |#
#|  This Version Supports Remote Code/Command Execution, XSS  |#
#|  And SQL Injection.                                        |#
#|  Thanks @lnxg33k, @dia2diab @Aelhemily, @okamalo           |#
################################################################
"""

print(get_green + copyr + get_end)


def urls_or_list():
    url_or_list = input(" [!] Scan URL or List of URLs? [1/2]: ")
    if url_or_list == "1":
        url = input(" [!] Enter the URL: ")
        # if not url.startswith("http://"):
        # Thanks to Nu11 for the HTTP checker
        # print get_red+'''\n Invalid URL, Please Make Sure That The URL Starts With \"http://\" \n'''+get_end
        # exit()
        if "?" in url:
            rce_func(url)
            xss_func(url)
            error_based_sqli_func(url)
        else:
            print(
                get_red
                + "\n [Warning] "
                + get_end
                + get_bold
                + "%s" % url
                + get_end
                + get_red
                + " is not a valid URL"
                + get_end
            )
            print(
                get_red
                + " [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"
                + get_end
            )
            exit()
    if url_or_list == "2":
        urls_list = input(
            get_green + " [!] Enter the list file name .e.g [list.txt]: " + get_end
        )
        open_list = open(urls_list).readlines()
        for line in open_list:
            if "?" in line:
                links = line.strip()
                url = links
                print(get_green + " \n [!] Now Scanning %s" % url + get_end)
                rce_func(url)
                xss_func(url)
                error_based_sqli_func(url)
            else:
                links = line.strip()
                url = links
                print(
                    get_red
                    + "\n [Warning] "
                    + get_end
                    + get_bold
                    + "%s" % url
                    + get_end
                    + get_red
                    + " is not a valid URL"
                    + get_end
                )
                print(
                    get_red
                    + " [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"
                    + get_end
                )
        exit()


urls_or_list()
