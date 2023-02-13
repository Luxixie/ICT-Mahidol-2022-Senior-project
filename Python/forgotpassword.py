from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
import uuid

app = Flask(__name__)

@app.route('/forgetpassword', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        # check if the email address exists in the database
        user = User.query.filter_by(email=email).first()
        if user:
            # generate a unique token
            token = str(uuid.uuid4())
            # save the token in the database
            user.reset_token = token
            user.reset_token_expiration = datetime.datetime.now() + datetime.timedelta(hours=1)
            db.session.commit()
            # send the password reset link to the user's email address
            send_reset_link(email, token)
            return redirect(url_for('password_reset_sent'))
        else:
            # the email address is not in the database
            return redirect(url_for('forgot_password'))
    return render_template('forgot_password.html')

@app.route('/sendemail')
def password_reset_sent():
    return render_template('password_reset_sent.html')

@app.route('/newpassword/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # check if the token is valid and has not expired
    user = User.query.filter_by(reset_token=token, reset_token_expiration > datetime.datetime.now()).first()
    if user:
        if request.method == 'POST':
            # update the user's password
            password = request.form['password']
            user.set_password(password)
            user.reset_token = None
            user.reset_token_expiration = None
            db.session.commit()
            # redirect the user to the login page
            return redirect(url_for('login'))
        return render_template('reset_password.html')
    else:
        # the token is invalid or has expired
        return redirect(url_for('forgot_password'))

def send_reset_link(email, token):
    # send the password reset link to the user's email address
    message = f'Password Reset Link: http://localhost:8080/newpassword/{token}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('email@example.com', 'your_email_password')
    server.sendmail('email@example.com', email, message)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
