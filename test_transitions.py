from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/cane",methods = ['POST', 'GET','OPTIONS'])
def helloWorld():
  return "Hello, cross-origin-world!"

if __name__ == "__main__":
    app.run(debug=False,threaded=True)