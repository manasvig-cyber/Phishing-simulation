
🛡️ Phishing Simulation Project

>⚠️ For educational purposes only. Do not use this project on real users or systems without proper authorization.

This project demonstrates a basic phishing attack simulation setup intended for cybersecurity awareness and educational labs. It includes a cloned phishing site, a credential-capturing script, an email sender, and instructions for running everything on a local Apache server.

📁 Project Structure

- `index.html` – Cloned phishing login page
- `log.php` – Captures and stores submitted credentials
- `email_template.html` – HTML-formatted phishing email template
- `send_email.py` – Python script to send the email using Gmail SMTP
- `README.md` – Instructions and description of the setup

⚙️ Setup Instructions
 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

 2. Move Files to Apache Web Directory

bash
sudo cp site_clone/index.html /var/www/html/
sudo cp site_clone/log.php /var/www/html/


3. Start Apache Server

bash
sudo systemctl start apache2

4. Open Phishing Page in Browser

Visit:


http://localhost/index.html

 5. Update and Run Email Sender

 Open `send_email.py` and edit:

Sender email
Receiver email
Gmail App Password
Then run:

bash
python3 send_email.py

6. Check Captured Credentials

Captured credentials will be saved by `log.php`. You can find the data in:

/var/www/html/log.txt


(if the script is configured that way)

🛠️ Tools Used

Apache2 – Hosting phishing page on localhost
PHP – For backend credential logging (`log.php`)
Python 3 – For sending phishing emails (`send_email.py`)
HTML/CSS – Used for the phishing page and email template
Gmail SMTP – Email delivery using `smtp.gmail.com`


