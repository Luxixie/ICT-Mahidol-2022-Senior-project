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
        # Fetch user balance
        cur = mysql.connection.cursor()
        cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
        user_balance = cur.fetchone()[0]

        return render_template('index.html', user_balance=user_balance)
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
            cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
            user = cur.fetchone()
            session['balance'] = user[0]
            return redirect(url_for('index'))
        else:
            return 'Invalid login.'
    else:
        return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


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

@app.route('/view_transactions')
def view_transactions():

    #check for user session
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM transactions WHERE user_id = %s", (session['user_id'],))
    transactions = cur.fetchall()
    # print(transactions)  # print the transactions returned by the query
    cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
    user_balance = cur.fetchone()[0]
    
    cur.close()

    return render_template('transaction_history.html', transactions=transactions, user_balance=user_balance)


@app.route('/buy-sell-stock', methods=['GET', 'POST'])
def buy_sell_stock():
    # check for user session
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        stock_ticker = request.form['stock_ticker']
        shares = int(request.form['shares'])
        action = request.form['action']

        # Get stock information using yfinance library
        stock_info = yf.Ticker(stock_ticker).fast_info
        if stock_info is None:
            return 'Error: Could not retrieve stock information for the given ticker.'

        # Calculate the cost of the transaction
        cost = stock_info['lastPrice'] * shares

        # Set the timestamp from datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Store the transaction in the MySQL database
        cur = mysql.connection.cursor()

        # Update user balance and portfolio
        cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
        user_balance = cur.fetchone()[0]
        cur.execute("SELECT * FROM portfolio WHERE user_id = %s AND ticker = %s", (session['user_id'], stock_ticker))
        user_portfolio = cur.fetchone()

        if action == 'buy':
            if user_balance < cost:
                return 'Error: Not enough balance to make the purchase.'
            new_balance = user_balance - cost
            if user_portfolio is None:
                cur.execute("INSERT INTO portfolio (user_id, ticker, shares) VALUES (%s, %s, %s)", (session['user_id'], stock_ticker, shares))
            else:
                if user_portfolio[2] is not None and user_portfolio[2].isdigit():
                    current_shares = int(user_portfolio[2])
                else:
                    current_shares = 0
                new_shares = current_shares + shares
                cur.execute("UPDATE portfolio SET shares = %s WHERE id = %s", (new_shares, user_portfolio[0]))
        else:
            if user_portfolio is None or user_portfolio[2] is None or not user_portfolio[2].isdigit() or int(user_portfolio[2]) < shares:
                return 'Error: Not enough shares in portfolio to make the sale.'
            new_balance = user_balance + cost
            if int(user_portfolio[2]) == shares:
                cur.execute("DELETE FROM portfolio WHERE id = %s", (user_portfolio[0],))
            else:
                new_shares = int(user_portfolio[2]) - shares
                cur.execute("UPDATE portfolio SET shares = %s WHERE id = %s", (new_shares, user_portfolio[0]))
        # fix else => sell function 
        cur.execute("UPDATE users SET balance = %s WHERE uid = %s", (new_balance, session['user_id']))
        mysql.connection.commit()

        # Store the transaction in the MySQL database
        cur.execute("INSERT INTO transactions (user_id, ticker, shares, action, cost, timestamp) VALUES (%s, %s, %s, %s, %s, %s)", (session['user_id'], stock_ticker, shares, action, cost, timestamp))
        mysql.connection.commit()

        return 'Transaction successful.'
    else:
        return render_template('buy_sell_stock.html')

@app.route('/portfolio', methods=['GET'])
def portfolio():
    # check for user session
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()

    # get user account balance
    cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
    user_balance = cur.fetchone()[0]

    # get user portfolio
    cur.execute("SELECT ticker, SUM(shares), SUM(cost)/SUM(shares) FROM transactions WHERE user_id = %s GROUP BY ticker", (session['user_id'],))
    user_portfolio = cur.fetchall()

    # get current stock prices
    cost = {}
    for stock in user_portfolio:
        cost[stock[0]] = yf.Ticker(stock[0]).fast_info.get('lastPrice')

    # calculate total value of each stock in portfolio
    total_values = {}
    for stock in user_portfolio:
        total_values[stock[0]] = stock[1] * cost[stock[0]]

    # calculate total portfolio value
    total_portfolio_value = sum(total_values.values()) + user_balance

    # calculate total cost of each stock in portfolio
    total_costs = {}
    for stock in user_portfolio:
        total_costs[stock[0]] = stock[1] * stock[2]

    # calculate total cost of portfolio
    total_portfolio_cost = sum(total_costs.values()) + user_balance

    # calculate percentage gain or loss
    if total_portfolio_cost > 0:
        percentage_gain_loss = ((total_portfolio_value - total_portfolio_cost) / total_portfolio_cost) * 100
    else:
        percentage_gain_loss = 0

    # update the portfolio table with average total price and total number of shares
    for stock in user_portfolio:
        cur.execute("UPDATE portfolio SET total_price=%s, shares=(SELECT SUM(shares) FROM transactions WHERE user_id=%s AND ticker=%s) WHERE user_id=%s AND ticker=%s", (stock[2], session['user_id'], stock[0], session['user_id'], stock[0]))
        mysql.connection.commit()

    return render_template('portfolio.html', portfolio=user_portfolio, prices=cost, total_values=total_values, total_portfolio_value=total_portfolio_value, user_balance=user_balance, percentage_gain_loss=percentage_gain_loss)

if __name__ == '__main__':
    app.run(debug=True)