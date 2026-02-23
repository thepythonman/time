import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    try:
        x = requests.get("https://time.now/developer/api/ip")
        timezone = x.text
    except Exception as e:
        timezone = f"Error fetching timezone: {str(e)}"
    
    return f"<title>Time checker</title><h1>Welcome to the Time Checker</h1><p>Time Info:{timezone}</p>"

if __name__ == "__main__":
    app.run(debug=False)
