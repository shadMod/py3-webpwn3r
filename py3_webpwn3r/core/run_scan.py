#!/usr/bin/env python3

# Copyright (C) 2013 Ebrahim Hegazy
# Copyright (C) 2023 shadmod <info@shadmod.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from vulnz import Vulnz

from py3_webpwn3r.core.costants import ANSI_BOLD, ANSI_END, ANSI_GREEN
from py3_webpwn3r.core.run_copyr import print_copyr

if __name__ == "__main__":
    print_copyr()
    url_or_list = input("[!] Scan URL or List of URLs? [1/2]: ")
    if url_or_list == "1":
        url = input("[!] Enter the URL: ")
        vulnz = Vulnz(url.strip())
        vulnz.call_all_detection_payloads()
    elif url_or_list == "2":
        input_urls_list = input(
            f"{ANSI_GREEN}[!] Enter the list file name .e.g [list.txt]: {ANSI_END}"
        )
        with open(input_urls_list) as open_urls_list:
            urls_list = open_urls_list.readlines()
        for line in urls_list:
            url = line.strip()
            print(f"\n{ANSI_GREEN}[!] Now Scanning {url}{ANSI_END}")
            vulnz = Vulnz(url)
            vulnz.call_all_detection_payloads()
    else:
        print(f"\n{ANSI_BOLD}[!] Set wrong input{ANSI_END}")
    exit()
