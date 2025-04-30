from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Hello from {socket.gethostname()}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

