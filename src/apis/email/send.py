import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(destinatario, asunto, mensaje):
    remitente = "jostinezequiel09@gmail.com"
    password = "1v19514#"  # No uses tu contraseña normal

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.sendmail(remitente, destinatario, msg.as_string())
        servidor.quit()
        print("Correo enviado con éxito")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

# Prueba
if __name__ == "__main__":
    enviar_correo("justintaveras566@gmail.com", "La paja", "Este es un mensaje de prueba.")
