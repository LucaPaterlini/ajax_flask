from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/cane",methods = ['POST', 'GET'])
def helloWorld():
    fd=open("payload","r")
    s=fd.read().split('\n')
    return jsonify(s)

if __name__ == "__main__":
    app.run(debug=False,threaded=True)