import logging, smtplib, os
from log import *
from datetime import datetime
from email.message import EmailMessage

class Email():

    DIRETORIO = os.path.abspath(os.curdir)
    DATA_LOG = datetime.now().strftime('%d-%m-%Y')

    def __init__(self):
        self.log = Email.DIRETORIO + "\\logs\\" + Email.DATA_LOG + ".log"
        self.dataAtual = (datetime.today().strftime('%d/%m/%Y'))
        self.email_Remetente = "DIGITE AQUI O E-MAIL REMETENTE"
        self.senha_Remetente = "DIGITE AQUI A SENHA DO REMETENTE"
        self.email_Destinatario = "DIGITE AQUI O E-MAIL DESTINATÁRIO"
        self.email_Destinatario_Falha = "DIGITE AQUI O E-MAIL DESTINATÁRIO QUE VAI RECEBER O LOG COM O ERRO"
        
    def enviar_email(self):
        logging.info("Iniciando a função ENVIAR_EMAIL")
        msg = EmailMessage()
        msg['subject'] = self.dataAtual + ' - Baixa de Extratos (NOME DO BANCO AQUI)'

        corpo_email = f"""
        Bom dia,

        Foram baixados os Extratos e salvos no Servidor do Financeiro.

        Att,

        Robô
        """
    
        logging.info("Definindo o remetente")
        msg['from'] = self.email_Remetente
        logging.info("Definindo o destinatário")
        msg['to'] = self.email_Destinatario
        logging.info("Definindo o corpo do email")
        msg.set_content(str(corpo_email))
        logging.info("Definindo o servidor SMTP")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            logging.info("Autenticando no servidor SMTP")
            smtp.login(self.email_Remetente, self.senha_Remetente)
            logging.info("Enviando o email")            
            smtp.send_message(msg)        

    def enviar_email_falha(self):
        logging.info("Iniciando a função ENVIAR_EMAIL")
        logging.info("Criando o objeto email")
        msg = EmailMessage()
        msg['subject'] = 'ROBÔ - Retirada de Extratos (NOME DO BANCO AQUI) APRESENTOU ERRO'

        corpo_email = f"""
        Bom dia,

        Segue o Log em anexo para análise.

        Att,

        Robô
        """

        logging.info("Definindo o remetente")
        msg['from'] = self.email_Remetente
        logging.info("Definindo o destinatário")
        msg['to'] = self.email_Destinatario_Falha
        logging.info("Definindo o corpo do email")
        msg.set_content(str(corpo_email))
        msg.add_attachment(open(self.log, "r").read(), filename="log.txt")
        logging.info("Definindo o servidor SMTP")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            logging.info("Autenticando no servidor SMTP")
            smtp.login(self.email_Remetente, self.senha_Remetente)
            logging.info("Enviando o email")            
            smtp.send_message(msg)

if __name__ == "__main__":
    log = Log()
    email = Email()
    email.enviar_email()
    email.enviar_email_falha()