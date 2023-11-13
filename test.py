import smtplib
from email.mime.text import MIMEText

# Paramètres SMTP de Breevo
EMAIL_USER_TLS = True
EMAIL_HOST = 'smtp-relay.sendinblue.com' #'smtp.gmail.com'
EMAIL_HOST_USER = 'locars.mail@gmail.com'
EMAIL_HOST_PASSWORD = 'JB0H7rP2pqNLtUfE' #'buqa xtjo lfhe ncaa'
EMAIL_PORT = 587

# Adresse e-mail du destinataire
to_email = 'djef.91860@gmail.com'

# Création du message
subject = 'Test Email'
body = 'Ceci est un test d\'e-mail.'
message = MIMEText(body)
message['Subject'] = subject
message['From'] = EMAIL_HOST_USER
message['To'] = to_email

# Envoi de l'e-mail
with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
    server.starttls()  # Utilisez cette ligne si EMAIL_USE_TLS est True
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(EMAIL_HOST_USER, [to_email], message.as_string())