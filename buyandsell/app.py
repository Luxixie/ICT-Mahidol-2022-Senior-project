from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import yfinance as yf
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'tester'
app.secret_key = 'secret_key'

mysql = MySQL(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user:
            session['user_id'] = user[0]
            return render_template('index.html')
        else:
            return 'Invalid login.'
    else:
        return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    return render_template('logout.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        dob = request.form['dob']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password, email, dob) VALUES (%s, %s, %s, %s)", (username, password, email, dob))
        mysql.connection.commit()

        return 'User registered.'
    else:
        return render_template('register.html')

@app.route('/buy-sell-stock', methods=['GET', 'POST'])
def buy_sell_stock():
    #check for user session
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        stock_ticker = request.form['stock_ticker']
        shares = request.form['shares']
        action = request.form['action']

        # Get stock information using yfinance library
        stock_info = yf.Ticker(stock_ticker).fast_info
        if stock_info['lastPrice'] is None:
            return 'Error: Could not retrieve stock information for the given ticker.'

        # Calculate the cost of the transaction
        cost = stock_info['lastPrice'] * int(shares)

        # Set the timestamp from datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Store the transaction in the MySQL database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO transactions (user_id, ticker, shares, action, cost, timestamp) VALUES (%s, %s, %s, %s, %s, %s)", (session['user_id'], stock_ticker, shares, action, cost, timestamp))
        mysql.connection.commit()

        return 'Transaction successful.'
    else:
        return render_template('buy_sell_stock.html')


if __name__ == '__main__':
    app.run(debug=True)