from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


msg = MIMEMultipart()
texto = 'estou enviando um e-mail teste com Python'

senha =''
msg ['From'] = 'limaionesmar@gmail.com'
msg ['To'] = 'ionesmarlima@gmail.com'
msg ['Testando1'] = 'E-mail test'

msg.attach(MIMEText(texto,'plain'))

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(msg['From'], senha)
server.sendmail(msg['from'], msg['To'], msg.as_string())
server.quit()
print ('mensagem enviada com sucesso')