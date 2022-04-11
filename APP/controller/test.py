import re
from APP.persistence.bd import insert_log


def main():
    valid_information = extract_valid_information_of_file("log_trabajoya_prod.log")
    insert_information(valid_information)


def extract_valid_information_of_file(file_name):
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


def insert_information(data):
    for log in data:
        insert_log(log)


if __name__ == "__main__":
    main()
