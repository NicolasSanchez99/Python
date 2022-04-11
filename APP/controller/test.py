import re
from APP.persistence.bd import insert
from APP.persistence.bd import select

def loadDomain():
    lines = []
    date_all = []
    domain = []
    capital = []
    aux = []
    file = "log_trabajoya_prod.log"
    with open(file) as aux:
        for i, line in enumerate(aux.readlines()):
            if i == 20:
                break
            lines.append(line)
    len(lines)

    for i, lista in enumerate(lines):
        domain = re.findall(
            "([\d{4}\-\d{1,2}\-\d{1,2}\s\d{1,2}:\d{1,2}]+[[a-z0-9.:\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])",
            lines[i])
        if len(domain) == 0:
            continue
        else:
            settle = re.findall("[a-z._]+", domain[1])
            if len(settle) == 0:
                continue
            print(settle)


def loadLine():
    lines = []
    date_all = []
    domain = []
    capital = []
    aux = []
    file = "log_trabajoya_prod.log"
    with open(file) as aux:
        for i, line in enumerate(aux.readlines()):
            if i == 30:
                break
            lines.append(line)
    len(lines)

    for i, lista in enumerate(lines):
        domain = re.findall(
            "([A-Z[\d{4}\-\d{1,2}\-\d{1,2}\s\d{1,2}:\d{1,2}]+[[a-z0-9.:\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])",
            lines[i])
        if len(domain) == 0 or len(domain[1]) <=5:
            continue
        else:
            settleLine = re.findall("[0-9]+", domain[1])
            settle2Info = re.findall("[A-Z]\w*", domain[1])
            settleFecha = domain[0]
            settleUrl = re.findall("[a-z._]+", domain[1])
            print(settle2Info[0])
            #insert(settleFecha,settle2Info, settleUrl[0], settleLine[0])


if __name__ == "__main__":
    loadLine()
