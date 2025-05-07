import imaplib
import email
from email.header import decode_header
import os
import uuid
from django.core.files.base import ContentFile
from Brand_Config_Approval_Portal.settings import BASE_DIR  # adjust as needed

import django
django.setup()

from Brand_Config_Approval_Portal.core.models import Email,EmailAttachment

while True:
    # Connect to the mail server
    imap = imaplib.IMAP4_SSL("imap.yourmailserver.com")
    imap.login("your_email@example.com", "your_password")

    imap.select("INBOX")  # Select inbox

    # Fetch unread emails
    status, messages = imap.search(None, '(UNSEEN)')
    email_ids = messages[0].split()

    for mail_id in email_ids:
        _, msg_data = imap.fetch(mail_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = decode_header(msg["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode()

        sender = msg.get("From")
        
        exisitng_brands = ['oppo','vivo','xiaomi','realme','samsung']
        temp_subject = subject.lower()
        brand = 'N/A'

        for single_brand in exisitng_brands:
            if single_brand in temp_subject:
                brand = single_brand 

        # Save email
        email_obj = Email.objects.create(
            subject=subject or "No Subject",
            sender=sender or "N/A",
            brand= brand or 'N/A',  # You can write logic to infer brand if needed
            processed=False,
            rejected=False
        )

        # Handle attachments
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get("Content-Disposition") is None:
                continue

            filename = part.get_filename()
            if filename:
                file_data = part.get_payload(decode=True)
                attachment = EmailAttachment(
                    email=email_obj,
                    processed=False
                )
                attachment.attachment.save(filename, ContentFile(file_data))
                attachment.save()

        imap.store(mail_id, '+FLAGS', '\\Seen')

    # Cleanup
    imap.logout()
