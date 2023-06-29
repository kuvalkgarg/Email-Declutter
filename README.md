# Email Declutter Tool
This project focuses on automating the cleanup of unwanted emails from a specific sender in an email account using IMAP (Internet Message Access Protocol). By connecting to the IMAP server, logging in to the email account, and selecting the desired mailbox, the script searches for emails from a particular sender and deletes them. This automation simplifies the process of managing and organizing your email inbox.

# Languages and Frameworks/Libraries
The project is implemented in **Python**. It utilizes the following libraries:

  * **imaplib:** Used for connecting to the IMAP server, performing email search, and managing emails.
  * **email:** Used for parsing email content and working with email messages.

# Installation and Execution
1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.0 or above).
3. Open a terminal or command prompt and navigate to the project directory.
4. Install the required dependencies by running the following command:
```
pip install imaplib
```
5. Open the script file (**email_declutter.py**) and update the following variables with your email account details:
  * **imap_server:** The IMAP server address (e.g., 'imap.gmail.com').
  * **imap_port:** The IMAP server port (e.g., 993).
  * **email_address:** Your email address.
  * **password:** Your email account password.
  * **sender_email:** The email address of the sender whose emails you want to delete.
  * **mailbox:** The mailbox/folder where you want to search and delete emails (e.g., 'INBOX', 'Spam').
6. Save the changes to the script file.
7. Run the Python script by executing the following command:
```
python email_declutter.py
```

# Conclusion
This project provides a simple solution for automating the cleanup of unwanted emails from a specific sender in your email account using IMAP. By specifying the IMAP server details, email credentials, and the target sender's email address, the script connects to the email server, performs the search, and deletes the identified emails. This automation saves time and effort in managing and organizing your email inbox.
