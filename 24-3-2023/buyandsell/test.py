from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'yourusername'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'yourdatabase'

mysql = MySQL(app)

# Company profiles
company_profiles = {
    'AAPL': {
        'name': 'Apple Inc.',
        'description': 'Apple Inc. is an American multinational technology company that specializes in consumer electronics, computer software, and online services. The company is known for its innovative hardware, including the iPhone, iPad, and Mac computers, as well as software such as the iOS and macOS operating systems and the iTunes media player. Apple was founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne and is headquartered in Cupertino, California.'
    },
    'MSFT': {
        'name': 'Microsoft Corporation',
        'description': 'Microsoft Corporation is an American multinational technology company that develops, licenses, and sells computer software, consumer electronics, and personal computers. Its best-known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. The company was founded in 1975 by Bill Gates and Paul Allen and is headquartered in Redmond, Washington.'
    },
    'AMZN': {
        'name': 'Amazon.com Inc.',
        'description': 'Amazon.com Inc. is an American multinational technology company that focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. The company is best known for its online retail platform, which sells a wide range of products and services worldwide. Amazon was founded in 1994 by Jeff Bezos and is headquartered in Seattle, Washington.'
    }
}

# Insert company profiles into database
@app.route('/')
def insert_profiles():
    try:
        cur = mysql.connection.cursor()

        for ticker, profile in company_profiles.items():
            name = profile['name']
            description = profile['description']
            cur.execute("INSERT INTO company_profiles (ticker, name, description) VALUES (%s, %s, %s)", (ticker, name, description))
            mysql.connection.commit()

        cur.close()
        return 'Company profiles inserted successfully!'

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

