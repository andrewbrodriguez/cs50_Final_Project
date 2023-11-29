from flask import render_template, session, redirect
from functools import wraps

def apology(message, code=400):
    """Render error message"""

    return render_template("apology.html", top=code, bottom=message)


def login_required(f):
    """Decorate routes to require login."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function