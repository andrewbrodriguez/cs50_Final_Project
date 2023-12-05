import re
import os
import json

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from main import run

# Configure app
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Modifies the HTTP response headers to prevent caching
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Show home page"""

    return render_template("index.html")

@app.route("/input", methods=["GET", "POST"])
@login_required
def input():
    """Input story text to be converted"""

    if request.method == "POST":
        # Send story to backend
        story = str(request.form.get("input"))
        if len(story) < 100 or len(story)>5000:
            return render_template("apology.html", message="Please enter a story over 100 characters in length, and under 5000 characters in length!")
        
        run(story)
        
        db.execute("UPDATE users SET num_runs = num_runs + 1 WHERE id = :user_id", user_id=session["user_id"])
        
        # Redirect user to results page
        return redirect("/results")

    return render_template("input.html")

@app.route("/results")
@login_required
def results():
    """Show images that result from story input"""

    file_paths = []
    for files in os.walk("static/images"):
        for file_name in files:
            file_paths.append(file_name)
    file_paths = file_paths[2]
    file_paths.sort(key = str)

    with open('blocks.json', 'r') as json_file:
        blocks = json.load(json_file)


    data = []
    counter = 0
    for file in file_paths:
        image_text_pairing = ("/static/images/" + file, blocks[counter])
        data.append(image_text_pairing)
        counter +=1



    return render_template("results.html", data=data)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("apology.html", message="You must provide your username!")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("apology.html", message="You must provide your password!")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("apology.html", message="Invalid login credentials!")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")


        # Ensure username was submitted and doesn't exist already
        if not username:
            return render_template("apology.html", message="You must provide your username!")
            
        # Ensure password has one number and one special character
        if not re.search("[0-9]", password) or not re.search("[!@#$%^&*()]", password):
            return render_template("apology.html", message="Your password must have at least one number and one special character!")

        if password != confirmation:
            return render_template("apology.html", message="Password and confirmation must match!")

        # Insert the new user into the database
        hsh = generate_password_hash(password)

        # Save user data, including time registered
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username, hash=hsh)

        except ValueError:
            return render_template("apology.html", message="This username already exists!")

    else:
        return render_template("register.html")

    session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", username)[0]["id"]
    return redirect("/")

@app.route("/stats", methods=["GET", "POST"])
def stats():
    """Display all users stats"""

    rows = db.execute("SELECT username, time, num_runs FROM users ORDER BY num_runs DESC")
    return render_template("stats.html", rows=rows,)