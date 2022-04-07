#File managment
from APP.persistence import bd
import re
file = "log_trabajoya_prod.log"
lines = []
date_all=[]
domain=[]
capital=[]
with open(file) as aux:
    for i, line in enumerate(aux.readlines()):
        if i ==10:
            break
        lines.append(line)
len(lines)
lineO = lines[1]
for i, lista in enumerate(lines):
    date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", lines[i])
    domain = re.findall("([[a-z0-9\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])", lines[i])
    if "INFO"  in lines[i]:
        print("SI")
    else:
        print("No")

    ##print(domain[1:])

## persistence integration

##bd.persistence.insert()