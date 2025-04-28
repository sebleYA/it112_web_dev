from flask import Flask, request, render_template
import random
from flask_sqlalchemy import SQLAlchemy


# create database and connect to sqlite
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# define cake model that maps item to a cake database
class Cake (db.Model):
    id = db.Column(db.Integer, primary_key=True) # auto incrementing ID
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    recipe = db.Column (db.Text, nullable=False)

with app.app_context():
    db.create_all()

    # populate database with items
    if Cake.query.count() == 0:
        cakes_sample = [
            {"title": "Chocolate Cake", "description": "A rich, moist chocolate cake topped with creamy chocolate frosting.", "recipe": "chocolate, cocoa powder, oil/butter, eggs, flour, baking powder, salt, sugar, milk, vanila extract"},
            {"title": "Vanilla Cake", "description": "A light and fluffy vanilla cake with a soft, whipped cream topping.", "recipe": 'all pupose flour, sugar, butter, eggs, baking powder, buttermilk, vanilla extract'},
            {"title": "Carrot Cake", "description": "A flavorful cake with grated carrots, walnuts, and cinnamon, topped with cream cheese frosting.", "recipe": "self rising flour, baking powder, sugar, oil, carrots"},
            {"title": "Lemon Cake", "description": "A refreshing lemon cake with a tart lemon glaze.", "recipe": "sugar, butter, eggs, vanilla extract, all purpose flour, baking powder, lemon zest"}
        ]

        for cake in cakes_sample:
            new_cake = Cake(title=cake['title'], description=cake['description'], recipe=cake['recipe'])
            db.session.add(new_cake)

        db.session.commit()

#create route that shows all lists of cake
@app.route('/cakes')
def cakes():
    cakes = Cake.query.all()
    return render_template('index.html', cakes=cakes)

# create detail route showing all full information for each

@app.route('/cake/<int:id>')
def cake_detail(id):
    cake = Cake.query.get_or_404(id) #get cake by id if not found return 404
    return render_template('cake_detail.html', cake = cake)



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
    app.run(host = '0.0.0.0', port=3500, debug=True) # created this because i keep getting access denied errors
