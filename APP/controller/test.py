import re
from APP.persistence.bd import insert_log
from APP.persistence.bd import create_bd
from APP.persistence.bd import create_table
from  APP.model.sqlModel import baseSQL


def main():
    valid_information = extract_valid_information_of_file("log_trabajoya_prod.log")
    insert_information(valid_information)


def extract_valid_information_of_file(file_name):
    try:
        valid_information = []

        with open(file_name) as file:
            for line in file.readlines():
                maches = re.findall("(\[(.+)\] ([A-Z]+) \[(.+):(.+)\]) ", line)
                if maches:
                    valid_information.append({
                        'datetime': maches[0][1],
                        'type_message': maches[0][2],
                        'filepath': maches[0][3],
                        'line': maches[0][4],
                    })

        return valid_information
    except FileNotFoundError:
        print("No file was found")


def insert_information(data):
    for log in data:
        insert_log(log)



if __name__ == "__main__":
    #scan = input('INGRESE NOMBRE DE ARCHIVO')
   # extract_valid_information_of_file(scan)
    base = baseSQL()
    base.file= "base.db"
    create_bd(base.file)




