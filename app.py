import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route("/")
def start():
    session['currency'] = 0
    session['streak'] = 0
    session['complete'] = False  # Ensure `complete` is initialized here
    return render_template("welcome.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/home")
def home():
    if 'currency' not in session:
        session['currency'] = 0
        session['streak'] = 0
        session['complete'] = False  # Ensure default value for session['complete']

    # Retrieve the completed state from the session
    completed = session.get('complete', False)

    return render_template("layout.html", 
                           currency=session['currency'], 
                           streak=session['streak'], 
                           completed=completed)


@app.route("/submit", methods=["GET"]) 
def gain_1():
    """Gain score"""
    print("Submit route hit")
    if 'currency' in session:
        session['currency'] += random.randrange(5, 15)
        session['streak'] += 1
        session['complete'] = True  # Store the complete state in session

    return redirect('/home')  # Removed query parameter

if __name__ == "__main__":
    app.run(debug=True)
