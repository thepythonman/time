import requests
x= requests.get("https://time.now/developer/api/ip")
timezone= x.text
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return f"<title>Time checker</title><h1>Welcome to the Time Checker</h1><p>Time Info:{timezone}</p>"



if __name__ == "__main__":
    app.run(debug=True)