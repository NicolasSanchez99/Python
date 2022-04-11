from APP.controller.file_controller import file_controller
from APP.persistence.bd import insert
from APP.persistence.bd import select

if __name__ == "__main__" :
        fl= file_controller()
        file = "log_trabajoya_prod.log"
        fl.load(file)
        print('-----------')
        fl.loadDomain(file)
        print('-------------')
        fl.loadMessage(file)
        print('-------------')
        fl.loadLine(file)
        print('-------------')
        select()

