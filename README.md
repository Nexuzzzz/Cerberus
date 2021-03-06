```c
   sSSs    sSSs   .S_sSSs     .S_SSSs      sSSs   .S_sSSs     .S       S.     sSSs  
 d%%SP   d%%SP  .SS~YS%%b   .SS~SSSSS    d%%SP  .SS~YS%%b   .SS       SS.   d%%SP  
d%S'    d%S'    S%S   `S%b  S%S   SSSS  d%S'    S%S   `S%b  S%S       S%S  d%S'    
S%S     S%S     S%S    S%S  S%S    S%S  S%S     S%S    S%S  S%S       S%S  S%|     
S&S     S&S     S%S    d*S  S%S SSSS%P  S&S     S%S    d*S  S&S       S&S  S&S     
S&S     S&S_Ss  S&S   .S*S  S&S  SSSY   S&S_Ss  S&S   .S*S  S&S       S&S  Y&Ss    
S&S     S&S~SP  S&S_sdSSS   S&S    S&S  S&S~SP  S&S_sdSSS   S&S       S&S  `S&&S   
S&S     S&S     S&S~YSY%b   S&S    S&S  S&S     S&S~YSY%b   S&S       S&S    `S*S  
S*b     S*b     S*S   `S%b  S*S    S&S  S*b     S*S   `S%b  S*b       d*S     l*S  
S*S.    S*S.    S*S    S%S  S*S    S*S  S*S.    S*S    S%S  S*S.     .S*S    .S*P  
 SSSbs   SSSbs  S*S    S&S  S*S SSSSP    SSSbs  S*S    S&S   SSSbs_sdSSS   sSS*S   
  YSSP    YSSP  S*S    SSS  S*S  SSY      YSSP  S*S    SSS    YSSP~YSSY    YSS'    
                SP          SP                  SP                                 
                Y           Y                   Y                                  
   ```                                                                                

<!-- yes i did steal some of these from MHDDoS, lel -->
<p align="center">
    <img alt="button-code-size-mb" src="https://img.shields.io/github/languages/code-size/Nexuzzzz/Cerberus" />
    <img alt="button-license" src="https://img.shields.io/github/license/Nexuzzzz/Cerberus">
    <img alt="button-file-count" src="https://img.shields.io/github/directory-file-count/Nexuzzzz/Cerberus">
    <img alt="button-forks" src="https://img.shields.io/github/forks/Nexuzzzz/Cerberus">
    <img alt="button-stars" src="https://img.shields.io/github/stars/Nexuzzzz/Cerberus">
    <img alt="button-issues" src="https://img.shields.io/github/issues/Nexuzzzz/Cerberus">
    <img alt="button-last-commit" src="https://img.shields.io/github/last-commit/Nexuzzzz/Cerberus/main">
</p>

# Cerberus
Cerberus is a layer 7 network stress testing tool that has a wide variety of normal and exotic attack vectors. <br>
It's written in Python3 and is usable on all systems with Python installed.

# Attack methods/vectors
```
GOLDENEYE: GoldeneEye dos tool, written by Jan Seidl
MIX: HTTP flood that randomly picks a http method
PROXY: HTTP GET flood, using a specified file with proxies
ARME: HTTP Apache Remote Memory Exhaustation (ARME) flood
HEAD: HTTP HEAD flood
OVERLOAD: HTTP GET flood that fills the headers dictionary with lots of junk data
FAST: HTTP GET flood that just targets "/", good for volumetric attacks
WEBSOCK: Websocket flood, supports SSL (wss://)
WATERTORTURE: DNS watertorture attack
COOKIE: HTTP GET flood with large cookies, tasty!
LEECH: Exotic bandwidth draining flood, keep the thread count below <5 and use residential proxies for better results
RECURSIVE: Recursive HTTP GET flood, very nasty
GHP: HTTP GET/HEAD/POST flood
BLAZINGFAST: Blazingfast bypass, impersonates the analytics bot which is allowed by default. Credits to 0x44F and mSQL
CLOUDFLARE: Cloudflare UAM/IUAM bypass using cloudscraper
POST: HTTP POST flood
XERXES: TCP connection flood, abusing the TOR network
MIMICK: HTTP GET flood that impersonates common web scrapers like Googlebot, Yahoo! Slurp or BaiduSpider
CONNECT: HTTP CONNECT flood
TOR: HTTP GET flood over TOR
DDG: HTTP GET DDoSGuard bypass
OPENREDIRECT: HTTP flood which abuses the Open Redirect vulnerability
HEX: HTTP GET flood that has a huge HEX string in the Host: header
GET: HTTP GET flood
```

# Notes
- Cloudflare bypass can't solve v2 challenges, so is therefore pretty much useless

# Depencies
- Python 3.6 or higher
- Everything can be installed with the `setup.py` script:
    - `python3 setup.py`

# Contributing
If you want to contribute, you can do so by 
- Creating a new method, more information can be found in `src/methods`
- Creating a pull request
- Making an issue with a new idea, or a code enhancement. I'll gladly look into them!
- Donating to me:
   - XMR: `4BFpJ8hEUBBUE8vKUq6arUhRNkmQbPFMG38tDJHroAiTcENF2oCjYgoeHRJg6ULcs42EZ1ynCGj6RVhBTBQ3BcRmKAP1ZRb`

# License
```sh
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
```
