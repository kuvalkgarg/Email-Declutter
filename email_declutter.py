import imaplib
import email

# IMAP server details
imap_server = 'imap.gmail.com'
imap_port = 993

# Your email credentials
email_address = 'username@email.com'
password = 'password'

# Connect to the IMAP server
imap = imaplib.IMAP4_SSL(imap_server, imap_port)

# Login to your email account
imap.login(email_address, password)

# Select the mailbox (e.g., 'INBOX')
mailbox = 'Spam'
imap.select(mailbox)

# Search for emails from the specific sender
sender_email = 'noreply@digest.groww.in'
status, response = imap.search(None, f'(FROM "{sender_email}")')

if status == 'OK':
    email_ids = response[0].split()

    # Iterate over each email and delete it
    for email_id in email_ids:
        # Set the email as deleted
        imap.store(email_id, '+FLAGS', '\\Bin')

    # Permanently remove the deleted emails
    imap.expunge()
    print(f"Deleted {len(email_ids)} email(s) from {sender_email}.")

# Logout and close the connection
imap.logout()
