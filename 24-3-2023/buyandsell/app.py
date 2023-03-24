from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import yfinance as yf
import datetime
# from decimal import Decimal

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
            if user_portfolio is None:
                return 'Error: Stock not found in portfolio.'
            current_shares = int(user_portfolio[2]) if user_portfolio[2] is not None and user_portfolio[2].isdigit() else 0
            if current_shares < shares:
                return 'Error: Not enough shares in portfolio to make the sale. Current shares: {}'.format(current_shares)
            new_balance = user_balance + cost
            if current_shares == shares:
                cur.execute("DELETE FROM portfolio WHERE id = %s", (user_portfolio[0],))
            else:
                new_shares = current_shares - shares
                cur.execute("UPDATE portfolio SET shares = %s WHERE id = %s", (new_shares, user_portfolio[0]))


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
    cur.execute("SELECT ticker, SUM(shares), SUM(cost) FROM transactions WHERE user_id = %s GROUP BY ticker", (session['user_id'],))
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
        total_costs[stock[0]] = stock[2]

    # calculate total cost of portfolio
    total_portfolio_cost = sum(total_costs.values())

    # calculate percentage gain or loss
    if total_portfolio_cost > 0:
        percentage_gain_loss = ((total_portfolio_value - total_portfolio_cost) / total_portfolio_cost) * 100
    else:
        percentage_gain_loss = 0

    # update the portfolio table with average total price
    for stock in user_portfolio:
        cur.execute("UPDATE portfolio SET total_price=%s WHERE user_id=%s AND ticker=%s", (cost[stock[0]], session['user_id'], stock[0]))
        mysql.connection.commit()

    return render_template('portfolio.html', portfolio=user_portfolio, prices=cost, total_values=total_values, total_portfolio_value=total_portfolio_value, user_balance=user_balance, percentage_gain_loss=percentage_gain_loss)



if __name__ == '__main__':
    app.run(debug=True)





# @app.route('/buy-sell-stock', methods=['GET', 'POST'])
# def buy_sell_stock():
#     # check for user session
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     if request.method == 'POST':
#         stock_ticker = request.form['stock_ticker']
#         shares = int(request.form['shares'])
#         action = request.form['action']

#         # Get stock information using yfinance library
#         stock_info = yf.Ticker(stock_ticker).fast_info
#         if stock_info is None:
#             return 'Error: Could not retrieve stock information for the given ticker.'

#         # Calculate the cost of the transaction
#         cost = stock_info['lastPrice'] * shares

#         # Set the timestamp from datetime
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         # Store the transaction in the MySQL database
#         cur = mysql.connection.cursor()

#         # Update user balance and portfolio
#         cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
#         user_balance = cur.fetchone()[0]
#         cur.execute("SELECT * FROM portfolio WHERE user_id = %s AND ticker = %s", (session['user_id'], stock_ticker))
#         user_portfolio = cur.fetchone()

#         if action == 'buy':
#             if user_balance < cost:
#                 return 'Error: Not enough balance to make the purchase.'
#             new_balance = user_balance - cost
#             if user_portfolio is None:
#                 cur.execute("INSERT INTO portfolio (user_id, ticker, shares, fifo_cost, fifo_shares) VALUES (%s, %s, %s, %s, %s)",
#                             (session['user_id'], stock_ticker, shares, cost, shares))
#             else:
#                 if user_portfolio[3] is None or user_portfolio[4] is None:
#                     cur.execute("UPDATE portfolio SET fifo_cost = %s, fifo_shares = %s WHERE id = %s", (cost, shares, user_portfolio[0]))
#                 else:
#                     fifo_cost = user_portfolio[3]
#                     fifo_shares = user_portfolio[4]
#                     new_shares = fifo_shares + shares
#                     new_cost = fifo_cost + cost
#                     new_fifo_cost = new_cost / new_shares
#                     cur.execute("UPDATE portfolio SET shares = %s, fifo_cost = %s, fifo_shares = %s WHERE id = %s",
#                                 (new_shares, new_fifo_cost, new_shares, user_portfolio[0]))
#         if action == 'sell':
#             # Calculate the profit/loss from selling shares using FIFO method
#             if user_portfolio is None:
#                 return 'Error: Stock not found in portfolio.'
#             current_shares = int(user_portfolio[2]) if user_portfolio[2] is not None and user_portfolio[2].isdigit() else 0
#             if current_shares < shares:
#                 return 'Error: Not enough shares in portfolio to make the sale. Current shares: {}'.format(current_shares)
#             cur.execute("SELECT * FROM transactions WHERE user_id = %s AND ticker = %s AND action = 'buy' ORDER BY timestamp ASC",
#                         (session['user_id'], stock_ticker))
#             buy_transactions = cur.fetchall()
#             sold_shares = 0
#             for transaction in buy_transactions:
#                 if sold_shares >= shares:
#                     break
#                 if transaction[3] > (shares - sold_shares):
#                     remaining_shares = transaction[3] - (shares - sold_shares)
#                     remaining_cost = remaining_shares * transaction[5] / transaction[3]
#                     cur.execute("UPDATE transactions SET shares = %s, cost = %s WHERE id = %s", (remaining_shares, remaining_cost, transaction[0]))
#                     sold_shares += (shares - sold_shares)
#                 else:
#                     sold_shares += transaction[3]
#                     cur.execute("DELETE FROM transactions WHERE id = %s", (transaction[0],))
#             if sold_shares < shares:
#                 return 'Error: Not enough shares in portfolio to make the sale. Current shares: {}'.format(current_shares)
#             sold_cost = 0
#             for transaction in buy_transactions:
#                 if shares <= 0:
#                     break
#                 if transaction[3] > shares:
#                     sold_cost += shares * transaction[5] / transaction[3]
#                     remaining_shares = transaction[3] - shares
#                     remaining_cost = remaining_shares * transaction[5] / transaction[3]
#                     cur.execute("UPDATE transactions SET shares = %s, cost = %s WHERE id = %s", (remaining_shares, remaining_cost, transaction[0]))
#                     shares = 0
#                 else:
#                     sold_cost += transaction[5]
#                     cur.execute("DELETE FROM transactions WHERE id = %s", (transaction[0],))
#                     shares -= transaction[3]

#             # Update user balance and portfolio
#             new_balance = user_balance + sold_cost
#             cur.execute("UPDATE users SET balance = %s WHERE uid = %s", (new_balance, session['user_id']))
#             cur.execute("SELECT * FROM portfolio WHERE user_id = %s AND ticker = %s", (session['user_id'], stock_ticker))
#             user_portfolio = cur.fetchone()
#             if user_portfolio[2] == sold_shares:
#                 cur.execute("DELETE FROM portfolio WHERE id = %s", (user_portfolio[0],))
#             else:
#                 new_shares = user_portfolio[2] - sold_shares
#                 cur.execute("UPDATE portfolio SET shares = %s WHERE id = %s", (new_shares, user_portfolio[0]))

#             mysql.connection.commit()

#         return 'Transaction successful.'
#     else:
#         return render_template('buy_sell_stock.html')
    

    #use 
# @app.route('/portfolio')
# def portfolio():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     cur = mysql.connection.cursor()

#     # Get the user's account balance
#     cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
#     user_balance = cur.fetchone()[0]

#     # Get the user's portfolio
#     cur.execute("SELECT ticker, SUM(shares), SUM(cost)/SUM(shares) FROM transactions WHERE user_id = %s GROUP BY ticker", (session['user_id'],))
#     user_portfolio = cur.fetchall()

#     # Get the current stock prices
#     stocks = []
#     for stock in user_portfolio:
#         stock_data = yf.Ticker(stock[0]).fast_info
#         stock_data['ticker'] = stock[0]
#         stock_data['shares'] = stock[1]
#         stock_data['average_cost'] = stock[2]
#         stock_data['total_value'] = stock[1] * stock_data['lastPrice']
#         stock_data['total_cost'] = stock[1] * stock[2]
#         stocks.append(stock_data)

#     # Calculate the total portfolio value
#     total_portfolio_value = user_balance + sum(stock['total_value'] for stock in stocks)

#     # Calculate the total portfolio cost
#     total_portfolio_cost = user_balance + sum(stock['total_cost'] for stock in stocks)

#     # Calculate the percentage gain or loss
#     if total_portfolio_cost > 0:
#         percentage_gain_loss = ((total_portfolio_value - total_portfolio_cost) / total_portfolio_cost) * 100
#     else:
#         percentage_gain_loss = 0

#     return render_template('portfolio.html', stocks=stocks, user_balance=user_balance, total_portfolio_value=total_portfolio_value, percentage_gain_loss=percentage_gain_loss)




# @app.route('/portfolio')
# def portfolio():
#     # check for user session
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     cur = mysql.connection.cursor()

#     # get user's portfolio
#     cur.execute("SELECT * FROM portfolio WHERE user_id = %s", (session['user_id'],))
#     portfolio = cur.fetchall()

#     # create dictionary to store stock data
#     stocks = {}
#     total_gain_loss = 0
#     total_cost_basis = 0

#     # iterate through each stock holding
#     for holding in portfolio:
#         # get stock data
#         ticker = holding[1]
#         shares = holding[2]

#         # get transaction data for the stock
#         cur.execute("SELECT * FROM transactions WHERE user_id = %s AND ticker = %s ORDER BY timestamp ASC",
#                     (session['user_id'], ticker))
#         transactions = cur.fetchall()

#         # calculate cost basis and gain/loss using FIFO method
#         cost_basis = 0
#         sold_shares = 0
#         for transaction in transactions:
#             if transaction[4] == 'buy':
#                 # calculate cost basis for this transaction
#                 if shares <= sold_shares:
#                     break
#                 if transaction[3] > (shares - sold_shares):
#                     cost_basis += (shares - sold_shares) * transaction[5] / transaction[3]
#                     sold_shares = shares
#                 else:
#                     cost_basis += transaction[5]
#                     sold_shares += transaction[3]
#             else:  # transaction[4] == 'sell'
#                 # calculate gain/loss for this transaction
#                 if shares <= sold_shares:
#                     break
#                 if transaction[3] > (shares - sold_shares):
#                     gain_loss = (shares - sold_shares) * (transaction[5] / transaction[3] - cost_basis)
#                     total_gain_loss += gain_loss
#                     total_cost_basis += (shares - sold_shares) * cost_basis
#                     sold_shares = shares
#                 else:
#                     gain_loss = transaction[5] - transaction[3] * cost_basis / shares
#                     total_gain_loss += gain_loss
#                     total_cost_basis += transaction[3] * cost_basis / shares
#                     sold_shares += transaction[3]

#         # add stock data to dictionary
#         stocks[ticker] = {'shares': shares, 'cost_basis': cost_basis, 'current_price': yf.Ticker(ticker).info['regularMarketPrice']}

#     # calculate total portfolio value and percentage gain/loss
#     total_portfolio_value = sum([stocks[ticker]['shares'] * stocks[ticker]['current_price'] for ticker in stocks])
#     percentage_gain_loss = total_gain_loss / total_cost_basis * 100 if total_cost_basis != 0 else 0

#     return render_template('portfolio.html', stocks=stocks, total_value=total_portfolio_value, total_gain_loss=total_gain_loss, percentage_gain_loss=percentage_gain_loss, total_cost_basis=total_cost_basis)




#test 
# @app.route('/buy-sell-stock', methods=['GET', 'POST'])
# def buy_sell_stock():
#     # check for user session
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     if request.method == 'POST':
#         stock_ticker = request.form['stock_ticker']
#         shares = int(request.form['shares'])
#         action = request.form['action']

#         # Get stock information using yfinance library
#         stock_info = yf.Ticker(stock_ticker).fast_info
#         if stock_info is None:
#             return 'Error: Could not retrieve stock information for the given ticker.'

#         # Calculate the cost of the transaction
#         cost = stock_info['lastPrice'] * shares

#         # Set the timestamp from datetime
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         # Store the transaction in the MySQL database
#         cur = mysql.connection.cursor()

#         # Update user balance and portfolio
#         cur.execute("SELECT balance FROM users WHERE uid = %s", (session['user_id'],))
#         user_balance = cur.fetchone()[0]
#         cur.execute("SELECT * FROM portfolio WHERE user_id = %s AND ticker = %s", (session['user_id'], stock_ticker))
#         user_portfolio = cur.fetchone()

#         if action == 'buy':
#             if user_balance < cost:
#                 return 'Error: Not enough balance to make the purchase.'
#             new_balance = user_balance - cost
#             if user_portfolio is None:
#                 cur.execute("INSERT INTO portfolio (user_id, ticker, shares) VALUES (%s, %s, %s)", (session['user_id'], stock_ticker, shares))
#             else:
#                 if user_portfolio[2] is not None and user_portfolio[2].isdigit():
#                     current_shares = int(user_portfolio[2])
#                 else:
#                     current_shares = 0
#                 new_shares = current_shares + shares
#                 cur.execute("UPDATE portfolio SET shares = %s WHERE id = %s", (new_shares, user_portfolio[0]))
#         else:
#             if user_portfolio is None:
#                 return 'Error: Stock not found in portfolio.'
#             current_shares = int(user_portfolio[2]) if user_portfolio[2] is not None and user_portfolio[2].isdigit() else 0
#             if current_shares < shares:
#                 return 'Error: Not enough shares in portfolio to make the sale. Current shares: {}'.format(current_shares)
            
#             # Apply FIFO method to sell shares
#             sold_shares = 0
#             cur.execute("SELECT * FROM transactions WHERE user_id = %s AND ticker = %s AND action = 'buy' ORDER BY timestamp", (session['user_id'], stock_ticker))
#             buy_transactions = cur.fetchall()
#             for buy_transaction in buy_transactions:
#                 buy_shares = buy_transaction[3]
#                 if sold_shares + buy_shares <= shares:
#                     sold_shares += buy_shares
#                     cur.execute("DELETE FROM transactions WHERE id = %s", (buy_transaction[0],))
#                 else:
#                     remaining_shares = shares - sold_shares
#                     cur.execute("UPDATE transactions SET shares = %s WHERE id = %s", (buy_shares - remaining_shares, buy_transaction[0]))
#                     break
            
#             # Update user balance and portfolio
#             new_balance = user_balance + stock_info['lastPrice'] * sold_shares
#             if sold_shares == current_shares:
#                 cur.execute("DELETE FROM portfolio WHERE id = %s", (user_portfolio[0],))
#             else:
#                 cur.execute("UPDATE portfolio SET shares = %s WHERE id = %s", (current_shares - sold_shares, user_portfolio[0]))

#         # Insert transaction into transactions table
#         cur.execute("INSERT INTO transactions (user_id, ticker, action, shares, price, timestamp) VALUES (%s, %s, %s, %s, %s, %s)",
#                     (session['user_id'], stock_ticker, action, shares, stock_info['lastPrice'], timestamp))

#         # Update user balance
#         cur.execute("UPDATE users SET balance = %s WHERE uid = %s", (new_balance, session['user_id']))

#         # Commit changes and close cursor
#         mysql.connection.commit()
#         cur.close()

#         return redirect(url_for('portfolio'))

#     return render_template('buy_sell_stock.html')