#File managment
from turtledemo.chaos import line

from APP.persistence import bd
import re
class file_controller:
    def load(self,file):
        lines = []
        date_all = []
        domain = []
        capital = []
        aux = []
        with open(file) as aux:
            for i, line in enumerate(aux.readlines()):
                if i == 20:
                    break
                lines.append(line)
        len(lines)

        for i, lista in enumerate(lines):
            date_all = re.findall("(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", lines[i])
            print(date_all)


    def loadDomain(self,file):
        lines = []
        date_all = []
        domain = []
        capital = []
        aux = []
        with open(file) as aux:
            for i, line in enumerate(aux.readlines()):
                if i == 20:
                    break
                lines.append(line)
        len(lines)

        for i, lista in enumerate(lines):
            domain = re.findall("([[a-z0-9\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])", lines[i])
            if len(domain)==0:
                continue
            else:
                print(domain)


    def loadMessage(self,file):
        lines = []
        date_all = []
        domain = []
        capital = []
        aux = []
        with open(file) as aux:
            for i, line in enumerate(aux.readlines()):
                if i == 20:
                    break
                lines.append(line)
        len(lines)

        for i, lista in enumerate(lines):
            capital = re.findall("[A-Z]\w*", lines[i])
            print(capital[:1])
