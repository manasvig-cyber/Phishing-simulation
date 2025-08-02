# Phishing Project

This project is a basic phishing simulation setup used for learning purposes. It includes:

- A cloned login page
- A PHP script to capture credentials
- An email template
- A Python script to send phishing emails

> 🚨 For educational use only. Do **not** use this on real targets without permission.

---

## Files Included

- `site_clone/index.html` – Cloned phishing login page  
- `site_clone/log.php` – Captures and stores entered credentials  
- `email_template.html` – HTML template used in the phishing email  
- `send_email.py` – Sends the phishing email to targets

---

## How to Run

1. Clone the repository
2.Move cloned site to Apache server directory
3. Move log.php and index.html to root of Apache if needed
4. Start Apache server
5. Open the phishing page in browser
6. Update and run the email sender script
7. Check logs
Captured credentials will be saved by log.php.Captured credentials will be saved by log.php. You can access them in:
/var/www/html/

🛠️ Tools Used

Apache2 – For hosting the phishing site locally (/var/www/html)
Python3 – Used for the email sending script
HTTrack – For cloning target websites
PHP – log.php used to capture and store credentials
HTML/CSS – To design the email template and phishing page
Git – Version control and collaboration
Gmail SMTP – For sending phishing emails (via smtp.gmail.com)
Linux (Kali) – The operating system used for development

Author
Made by Deepthi452005
GitHub: https://github.com/Deepthi452005
