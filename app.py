import os

from flask import Flask

app = Flask(__name__)

name = os.environment.get('YOUR_NAME')


@app.route("/")
@app.route("/hello")
def main():
    print(name)
    return '''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Hello, ''' + name + '''!</h1>
            </body>
        </html>'''


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8082")
