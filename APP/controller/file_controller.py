#File managment
file = "log_trabajoya_prod.log"
lines = []
with open(file) as aux:
    for i, line in enumerate(aux.readlines()):
        if i ==10:
            break
        lines.append(line)
len(lines)
lineO = lines[1]
for i, lista in enumerate(lines):
    print(lines[i])
