from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return '''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Hello, world!</h1>
            </body>
        </html>'''


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
