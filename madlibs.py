"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    if request.args.get("answer") == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    nouns = [None]*4

    color = request.args.get("color")
    words = request.args.getlist("noun")

    index = 0
    for word in words:
        nouns[index] = word
        index += 1

    madlib_list = ['madlib.html', 'madlib1.html', 'madlib2.html']
    random_madlib = choice(madlib_list)
    adjective = request.args.get("adjective")
    person = request.args.get("person")
    return render_template(random_madlib, color=color, noun1=nouns[0],
                           adjective=adjective, person=person, noun2=nouns[1],
                           noun3=nouns[2], noun4=nouns[3])



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
