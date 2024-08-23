# flake8: noqa

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

from py3_webpwn3r.core.costants import ANSI_END, ANSI_GREEN


def print_copyr() -> None:
    copyr = f"""{ANSI_GREEN}
         __          __  _     _____                 ____       
         \ \        / / | |   |  __ \               |___ \      
          \ \  /\  / /__| |__ | |__) |_      ___ __   __) |_ __ 
           \ \/  \/ / _ \ '_ \|  ___/\ \ /\ / / '_ \ |__ <| '__|
            \  /\  /  __/ |_) | |     \ V  V /| | | |___) | |   
             \/  \/ \___|_.__/|_|      \_/\_/ |_| |_|____/|_|   

    ################################################################
    #| "WebPwn3r" Web Applications Security Scanner               |#
    #|  By Ebrahim Hegazy - @Zigoo0                               |#
    #|  This Version Supports Remote Code/Command Execution, XSS  |#
    #|  And SQL Injection.                                        |#
    #|  Thanks @lnxg33k, @dia2diab @Aelhemily, @okamalo           |#
    ################################################################
    {ANSI_END}
    """
    print(copyr)
