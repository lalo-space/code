import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import psutil

# Funzione per ottenere i dati SMART di un disco
def get_smart_data(device):
    command = ['smartctl', '-a', device]
    output = subprocess.check_output(command).decode('utf-8')
    return output

# Funzione per elaborare il report
def process_smart_report(device):
    smart_data = get_smart_data(device)
    
    # Elabora i dati SMART qui secondo le tue esigenze
    # Esempio: analizza le righe contenenti informazioni importanti come temperatura, errori, ecc.
    
    report = "Report per il disco {}:\n\n".format(device)
    report += smart_data
    report += "\n\n"
    
    return report

# Funzione per inviare l'output via email
def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Email inviata con successo")
    except Exception as e:
        print("Errore durante l'invio dell'email:", str(e))

# Esempio di utilizzo
sender_email = 'your_email@gmail.com'  # Inserisci il tuo indirizzo email
sender_password = 'your_password'  # Inserisci la password del tuo indirizzo email
receiver_email = 'recipient_email@gmail.com'  # Inserisci l'indirizzo email del destinatario
subject = 'Report SMART dei dischi'

# Ottieni la lista dei dischi presenti nel sistema
disks = psutil.disk_partitions()

# Elabora il report per ogni disco e aggiungilo al corpo dell'email
report = ""
for disk in disks:
    device = disk.device
    report += process_smart_report(device)

# Invia l'email con il report completo
send_email(sender_email, sender_password, receiver_email, subject, report)
