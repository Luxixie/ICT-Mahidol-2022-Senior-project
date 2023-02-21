from flask import Flask, render_template, jsonify, request
import yfinance as yf
import json
import plotly
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def index():
    symbol = request.args.get('symbol', 'SIRI.BK')
    data = yf.download(tickers=symbol, period='1d', interval='1m')
    line_chart = go.Scatter(x=data.index, y=data['Close'], name='Closing price', mode='lines')
    data_trace = [line_chart]
    layout = go.Layout(title='Real-time stock price chart for ' + symbol, xaxis=dict(title='Time'), yaxis=dict(title='Price'))
    fig = go.Figure(data=data_trace, layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', symbol=symbol, graphJSON=graphJSON)

@app.route('/update')
def update():
    symbol = request.args.get('symbol', 'SIRI.BK')
    data = yf.download(tickers=symbol, period='1d', interval='1m')
    last_price = data['Close'][-1]
    return jsonify(y=[last_price])

if __name__ == '__main__':
    app.run(debug=True)
