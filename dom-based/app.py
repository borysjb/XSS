from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # change in production


@app.route("/secret")
def secret():
    with open("flag.txt", "r") as flag:
        return flag.read(), 200, {"Content-Type": "text/plain"}

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # VERY basic authentication (demo only)
        if username=="user" and password=="user":
            session["user"] = username
            return redirect(url_for("account"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/account")
def account():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("account.html", username=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
