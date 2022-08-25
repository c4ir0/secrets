# I'm kind developer u can use my password in hack the planet 'jkj%%*Nmnkds' 
# or u can use the API-key that I left in the main code below

import sys
import re

f = open('E:\draft.txt', 'r')
text = f.read()
ips = []
API_kEy = 'dsadsasasc14521456sadsdsdd465sasadsad6545d4sa6d5sadda4564asd'
notsthuCANfindUSEFUL = '132ASasasadsadsadASaS(&*()&*&N'
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)
            print(match)

