from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, This is my flask app<h1>"

@app.route("/about")
def about():
    return "<p>Hi, welcome to my page, My name is Seblewongel but you can call me Seble<p>"


if __name__ == "__main__":
    app.run(debug=True)
