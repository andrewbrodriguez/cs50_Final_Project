import re
import json
import sys

from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from main import run

# Configure server
server = Flask(__name__)

# Configure session to use filesystem
server.config["SESSION_PERMANENT"] = False
server.config["SESSION_TYPE"] = "filesystem"
Session(server)

# Modifies the HTTP response headers to prevent caching
@server.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@server.route("/")
def index():
    """Show home page"""

    return render_template("index.html")

@server.route("/input", methods=["GET", "POST"])
@login_required
def input():
    """Input story text to be converted"""

    if request.method == "POST":
        # Send story to backend
        success = run(request.form.get("story"))

        if success is None:
            return apology("you must enter a story!")
        
        # Redirect user to results page
        return redirect("/results")

    return render_template("input.html")

@server.route("/results")
@login_required
def results():
    """Show images that result from story input"""

    return render_template("results.html")

@server.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("you must provide your username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("you must provide your password")

        # Query json for username and filter for username
        with open('users.json', 'r') as f:
            raw_data = json.load(f)
        data = [entry for entry in raw_data if entry.get('username') == request.form.get("username")]

        # Ensure username exists and password is correct
        if len(data) != 1 or not check_password_hash(data[0]["hash"], request.form.get("password")):
            return apology("invalid login credentials", 403)

        # Remember which user has logged in
        session["user_id"] = data[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@server.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@server.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted and doesn't exist already
        if not username:
            return apology("must provide username")

        # Query json for username and filter for username
        with open('users.json', 'r') as f:
            raw_data = json.load(f)
        data = [entry for entry in raw_data if entry.get('username') == request.form.get("username")]

        if len(data) == 1:
            return apology("this username already exists")

        if not re.search("[0-9]", password) or not re.search("[!@#$%^&*()]", password):
            return apology("password must have at least one number and one special character")

        if password != confirmation:
            return apology("password and confirmation must match")

        # Insert the new user into users.json
        new_user = {username: password}

        with open('users.json', 'w') as f:
            json.dump(new_user, f)

    else:
        return render_template("register.html")

    with open('users.json', 'r') as f:
        raw_data = json.load(f)
    session["user_id"] = [entry for entry in raw_data if entry.get('username') == request.form.get("username")][0]["id"]
    return redirect("/")