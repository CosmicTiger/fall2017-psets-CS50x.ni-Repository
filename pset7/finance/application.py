
# os for the utility of register the transaction_date
import os

from cs50 import SQL
from flask import Flask, flash, redirect, url_for, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# a utility function to verify about the cash availability of the user
def have_money(id_user, TOTAL):
    rows = db.execute("SELECT SUM(total) as Z FROM transactions WHERE id_user = ?", id_user)
    money = db.execute("SELECT cash FROM users WHERE id = ?", id_user)
    money = float(money[0]["cash"])
    if rows[0]["Z"] == None:
        return True
    if float(rows[0]["Z"]) + float(TOTAL) > money:
        return False
    else:
        return True


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    id_current_user = session.get("user_id")
    rows = db.execute(
       "SELECT symbol as Symbol, name as Name,sum(share) as Shares, avg(price) as Price, sum(total) as TOTAL FROM transactions WHERE id_user = ? group by symbol, price", id_current_user)

    if not rows:
        return apology("You doesn't possess transactions", 200)

    total = 0.0

    for row in rows:
        total = total + float(row["TOTAL"])

    money = db.execute("SELECT cash FROM users WHERE id = ?", id_current_user)
    return render_template("index.html", rows = rows, usd = usd, total = total, cash = (float(money[0]["cash"]) - total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("Complete fields")

        symbol = request.form.get("symbol")
        action = lookup(symbol)

        if not action:
            return apology("Symbol incorrect!!", 400)

        id_current_user = session.get("user_id")
        name = action["name"]

        try:
            share = int(request.form.get("shares"))
        except ValueError:
            return apology("Share incorrect!!", 400)

        price = float(action["price"])
        TOTAL = float(share * price)

        if share <= 0:
            return apology("share should be positive!")

        if not have_money(id_current_user, TOTAL):
            return apology("You don't have money to complete this transaction!")

        TOTAL = share * price

        db.execute("INSERT INTO transactions(id_user, symbol, name, share, price, total, transaction_date) VALUES(?,?,?,?,?,?, datetime('now'))",
                id_current_user, symbol, name, share, price, TOTAL)


        return redirect(url_for("index"))

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    rows = db.execute("SELECT symbol, name, share, price, transaction_date FROM transactions WHERE id_user = ?", session.get("user_id"))

    if not rows:
        return apology("History empty!!", code = 200)
    return render_template("history.html", transactions=rows, usd = usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")

        quoted = lookup(symbol)
        if quoted == None:
            return apology("Write a symbol correct")

        return render_template("quoted.html", quote=quoted)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # forget any user_id just in case
    session.clear()

    # waiting for the values that were inserted
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password was submitted
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("password do not match. please, do it again", 400)

        # Generate the hash encryption for the password formulated
        hash = generate_password_hash(request.form.get("password"))

        # Creates the new user which is going to enter at the database
        new_user_id = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                                    username=request.form.get("username"),
                                    hash=hash)

        # if the user already exists and unique username constraint violated, then
        if not new_user_id:
            return apology("username was already taken", 400)

        # remember the user in the session
        session["user_id"] = new_user_id

        # displaying a flash message
        flash("Registered was successful!")

        # user is redirected to home because of his first login after registration
        return redirect(url_for("index"))
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
       id_current_user = session.get("user_id")
       symbol = request.form.get("symbol")
       if not symbol:
           return apology("write a symbol!!", 400)
       action = lookup(symbol)
       if not action:
           return apology("Write a correct symbol!!", 401)

       shares = db.execute("SELECT SUM(share) AS Share FROM transactions WHERE id_user = ? and symbol = ?", id_current_user, symbol)
       shares = int(shares[0]["Share"])

       try:
           shares_for_sell = int(request.form.get("shares"))
       except ValueError:
           return apology("Share incorrect!!", 400)

       if shares_for_sell <= 0:
           return apology("shares should be positive!!", 400)

       if not request.form.get("shares").isnumeric() or int(request.form.get("shares")) < 1:
           return apology("Share incorrect!", 400)

       if shares_for_sell > shares:
           return apology("You sell more than you have!!", 400)

       name = action["name"]
       share = shares_for_sell * -1
       price = float(action["price"])
       TOTAL = share * price

       db.execute("INSERT INTO transactions(id_user,symbol,name,share,price,TOTAL,transaction_date) VALUES(?,?,?,?,?,?,datetime('now'))",
                   id_current_user, symbol, name, share, price, TOTAL)
       return redirect("/")
    elif request.method == "GET":
        symbols = db.execute("SELECT symbol FROM transactions WHERE id_user = :id_user", id_user = session["user_id"])
        return render_template("sell.html", symbols= symbols)

def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
