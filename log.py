import logging, time, os

class Log(object):
    def __init__(self):
        self.gerar_log()

    def gerar_log(self):
        self.diretorio_log()
        logging.basicConfig(filename= self.path + self.filename, 
                            filemode='w', 
                            level=logging.INFO, 
                            format="{asctime} - {levelname} - {funcName}:{lineno} - {message}",
                            datefmt="%d/%m/%Y %H:%M:%S",
                            style='{')

    def diretorio_log(self):
        data = time.strftime('%d-%m-%Y')
        self.path = 'logs/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            self.filename = data +'.log'
        else:
            self.filename = data +'.log'