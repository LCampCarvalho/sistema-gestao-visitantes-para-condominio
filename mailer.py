import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_notification(to_email, subject, message):
    # Configurações do Gmail
    from_email = 'condominio.solimar@gmail.com'
    from_password = 'XXXXXXX'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")
