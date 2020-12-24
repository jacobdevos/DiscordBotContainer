from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    if request.json:
        return "Hello Jake \n {}".format(request.json)
    else:
        return "hello world!"
@app.route("/jake", methods=['POST'])
def jake():
    if request.json:
        return request.json
    else:
        return "wut?"

if __name__ == "__main__":
    app.run(host="0.0.0.0")