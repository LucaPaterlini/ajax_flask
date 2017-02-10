from flask import Flask

app = Flask(__name__)
@app.route("/cane", methods=['GET', 'POST'])
def helloWorld():
  return "Hello, cross-origin-world!"
if __name__ == '__main__':
     app.run()