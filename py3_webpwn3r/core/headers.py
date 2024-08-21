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

# You should have recreived a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from urllib.request import urlopen, FancyURLopener

from costants import (
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
