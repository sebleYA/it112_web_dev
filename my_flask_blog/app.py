from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, This is my flask app<h1>"

@app.route("/about")
def about():
    return "<p>Hi, welcome to my page, My name is Seblewongel but you can call me Seble<p>"

# creating fortune list by colors

FORTUNES = {
    "red":[
        "Embrace yourself",
        "Be happy for what you have",
        "Love your work",
        "Success is around your corner",
    ],
    "green":[
        "Today is your lucky day",
        "Thursday is your day!",
        "Happiness brings new life.",
        "Select your Lottery today!",
    ],
    "blue":[
         "Avoid eating to much sugar",
        "Trying finishing your chores on time today.",
         "Be next to your loved ones.",
        "You are full energy.",
    ],
    "violet":[
        "Look up, your get your answer",
        "Be selective",
        "Your are #1",
        "Be patient, you will be rewarded", 
    ]
}

# route showing users choice and displaying fortune
@app.route("/fortune", methods = ["GET", "POST"])
def fortune():
    if request.method == "POST":
        print("Received POST request")
        print("Form data:", request.form)

        name = request.form.get('name')
        color = request.form.get('color')
        number = request.form.get('number')
        my_fortune= random.choice(FORTUNES.get(color, ['Your future is ... wait for it ...']))

        return render_template('fortune_result.html', name=name, fortune = my_fortune)

    return render_template('fortune_form.html')

        


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=3500, debug=True)
