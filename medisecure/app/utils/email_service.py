import smtplib
import os
from email.message import EmailMessage

def send_welcome_email(patient_name: str, patient_email: str):
    """The Engine: Assembles and dispatches an email via SMTP."""
    
    sender_email = os.getenv("MAIL_USERNAME")
    sender_password = os.getenv("MAIL_PASSWORD")
    
    if not sender_email or not sender_password:
        print("[BACKGROUND TASK ERROR] Missing email credentials in .env file.")
        return

    # 1. Assemble the Envelope
    msg = EmailMessage()
    msg['Subject'] = "Welcome to MediSecure Hospital"
    msg['From'] = sender_email
    msg['To'] = patient_email
    
    # 2. Write the Letter
    content = f"""
    Dear {patient_name},
    
    Welcome to the MediSecure Hospital network.
    Your patient profile has been successfully registered by our administration team.
    
    Please ensure you arrive 15 minutes prior to any scheduled appointments.
    
    Regards,
    The MediSecure Administration Team
    """
    msg.set_content(content)
    
    # 3. Connect to the Post Office and Send
    try:
        # Using Gmail's secure SSL port 465
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"[BACKGROUND TASK SUCCESS] Welcome email delivered to {patient_email}")
    except Exception as e:
        print(f"[BACKGROUND TASK ERROR] Failed to send email to {patient_email}: {e}")