import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

file = 'Diretorio do Email'

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'email@gmail.com'
smtp_password = 'codigo de apps permitidos google'

from_email = 'email'
to_email = 'email'
subject = 'Assunto'
body = 'Corpo do email'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))  # Tenha certeza que o conteudo do do email seja um texto

# Anexe arquivos, documentos
with open(file, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='pdf')
    attachment.add_header('Content-Disposition', 'attachment', filename='Nome_Do_Arquivo.pdf')
    msg.attach(attachment)

try:
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(msg)
    smtp.quit()
    print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar email: {e}")
