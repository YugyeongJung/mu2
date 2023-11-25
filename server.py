from flask import Flask # Flask
from flask_cors import CORS
from flask import request
import time

app = Flask(__name__)
CORS(app)

@app.route('/users')
def users():
    return { "id" : 1, "name" : "yerin" }

@app.route("/fileName", methods=["POST"])
def fileName():
    count = request.json['fileName']
    return { 'fileName': count }


@app.route("/ModelCheck", methods=["GET"])
def ModelCheck():
    #to be filled by Ainesh's code
    time.sleep(5)
    return {'result': 'temp result'}


@app.route("/Unlearning", methods=["GET"])
def Unlearning():
    #to be filled by Ainesh's code
    time.sleep(2)
    return {'result': 'temp result unlearns'}


if __name__ == "__main__":
    app.run(debug = True)
