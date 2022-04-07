#File managment
from turtledemo.chaos import line

from APP.persistence import bd
import re
file = "log_trabajoya_prod.log"
lines = []
date_all=[]
domain=[]
capital=[]
aux=[]
with open(file) as aux:
    for i, line in enumerate(aux.readlines()):
        if i ==20:
            break
        lines.append(line)
len(lines)
lineO = lines[1]
for i, lista in enumerate(lines):
    date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", lines[i])
    domain = re.findall("([[a-z0-9\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])", lines[i])
    capital = re.findall("[A-Z]\w*",lines[i])

    ##print(date_all)
    aux=domain[1:]
    aux[:1]
    print(domain[1:])
   # print(capital[:1])

## persistence integration

##bd.persistence.insert()