from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Email Configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587  # For TLS (change if necessary)
SMTP_USERNAME = 'errachdiamine56@gmail.com'  # Replace with your email address
SMTP_PASSWORD = 'ckmq xnog wvqp zpsi'  # Replace with your email password
EMAIL_FROM = 'errachdiamine56@gmail.com'  # Replace with your email address
EMAIL_TO = 'errachdiamine56@gmail.com'  # Replace with the recipient's email address
EMAIL_SUBJECT = 'New Contact Form Submission'

@app.route('/')
def form():
    return render_template('submit.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        message = request.form['message']

        # Prepare the email message
        email_body = f"Name: {name}\nLastName: {lastname}\nEmail: {email}\nMessage:\n{message}"
        msg = MIMEText(email_body)
        msg['Subject'] = EMAIL_SUBJECT
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        # Send the email
        try:
            smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            smtp.starttls()  # Enable TLS
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
            smtp.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            smtp.quit()
            return redirect("http://127.0.0.1:5000")
        except Exception as e:
            return f"Failed to send message. Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
