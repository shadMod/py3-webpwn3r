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

import logging
import re
import time
from urllib.request import urlopen

from costants import (
    ANSI_BLUE,
    ANSI_BOLD,
    ANSI_END,
    ANSI_GREEN,
    ANSI_RED,
    HTTP_HEADER_SERVER,
    HTTP_HEADER_SIG,
    PAYLOADS_AND_CHECK,
)
from user_agent import useragent

logger = logging.getLogger(__name__)


class Vulnz:
    def __init__(self, url: str):
        """Initializes a Vulnz instance.

        Args:
            url (str): Add me.
        """
        self._message = ""
        self.url = url

    def write_message(self, message: str | list, color: str | None = None) -> None:
        if isinstance(message, str):
            msg = f"{color}{message}{ANSI_END}" if color else f" {message}{ANSI_END}"
            self._message += msg
            logger.info(msg)
            print(msg)
        elif isinstance(message, list):
            for msg in message:
                self.write_message(msg, color)
        else:
            self.write_message("[!] Wrong type msg")

    def _main(self, payload_key: str) -> None:
        """Main function for Vulnz.

        Args:
            payload_key (str): Key for payload.
        """
        opener = urlopen(self.url)
        if opener.code == 999:
            # Detecting the WebKnight WAF from the StatusCode.
            self.write_message(
                [
                    "[~] WebKnight WAF Detected!",
                    "[~] Delaying 3 seconds between every request",
                ],
                ANSI_RED,
            )
            time.sleep(3)
        vuln = 0
        payloads_with_check = PAYLOADS_AND_CHECK.get(payload_key)
        if not payloads_with_check:
            self.write_message(f"[!] Payload key not correct", ANSI_RED)
            return

        # Used re.I to fix the case-sensitive issues like "payload" and "PAYLOAD".
        check = re.compile(payloads_with_check["check"], re.I)

        urls_params = self.url.split("?")
        if len(urls_params) <= 1:
            self.write_message(
                [
                    f"[Warning] {self.url} is not a valid URL, no query call is present",
                    "[Warning] You should write a Full URL - e.g. https://site.com/page.php?id=value",
                ],
                ANSI_RED,
            )
            return

        for params in urls_params[1].split("&"):
            for payload in payloads_with_check["payloads"]:
                bugs = self.url.replace(params, params + str(payload).strip())
                request = useragent.open(bugs)
                html = request.readlines()
                for line in html:
                    line_as_str = str(line)
                    checker = re.findall(check, line_as_str)
                    if len(checker) != 0:
                        self.write_message(f"[*] Payload: {payload}", ANSI_RED)
                        self.write_message(
                            f"[!] Code Snippet: {line.strip()}", ANSI_GREEN
                        )
                        self.write_message(f"[*] POC: {bugs}", ANSI_BLUE)
                        vuln += 1
        if vuln == 0:
            self.write_message("[!] Target is not vulnerable!", ANSI_GREEN)
        else:
            self.write_message(
                f"[!] Congratulations you've found {vuln} bugs :-) Happy Exploitation :D",
                ANSI_BLUE,
            )

    def get_server_headers(self):
        """This function will print the server headers such as WebServer OS & Version"""

        self.write_message(["[!] Fingerprinting the backend Technologies."], ANSI_BOLD)
        url_data = urlopen(self.url)
        if url_data.code == 200:
            self.write_message("[!] Status code: 200 OK", ANSI_GREEN)
        if url_data.code == 404:
            self.write_message(
                "[!] Page was not found! Please check the URL \n", ANSI_RED
            )
            exit()
        _server = url_data.headers.get(HTTP_HEADER_SERVER)
        _host = self.url.split("/")[2]
        self.write_message(
            [f"[!] Host: {_host}", f"[!] WebServer: {_server}"], ANSI_GREEN
        )
        for _, item in url_data.headers.items():
            for powered in item:
                if HTTP_HEADER_SIG in item:
                    self.write_message(f"[!] {str(powered).strip()}", ANSI_GREEN)

    def rce_vulnt(self) -> None:
        """Call up detection payloads to get for RCE vulnerabilities."""

        self.write_message(
            "[!] Now Scanning for Remote Code/Command Execution", ANSI_BOLD
        )
        self.write_message(
            "[!] Covering Linux & Windows Operating Systems, please wait...",
            ANSI_BLUE,
        )
        self._main("rce")

    def xss_vulnt(self) -> None:
        """Call up detection payloads to get for XSS vulnerabilities."""

        self.write_message("[!] Now Scanning for Cross-site scripting", ANSI_BOLD)
        self.write_message("[!] Please wait...", ANSI_BLUE)
        self._main("xss")

    def error_based_sqli_vulnt(self) -> None:
        """Call up detection payloads to get for Error-based SQLi."""

        self.write_message("[!] Now Scanning for Error Based SQL Injection", ANSI_BOLD)
        self.write_message(
            "[!] Covering MySQL, Oracle, MSSQL, MSACCESS & PostGreSQL Databases, please wait...",
            ANSI_BLUE,
        )
        self._main("error-based-sqli")

    def call_all_detection_payloads(self) -> None:
        """Call up detection payloads to get for all payloads."""

        self.rce_vulnt()
        self.xss_vulnt()
        self.error_based_sqli_vulnt()
