from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "12345":
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Credenciales incorrectas")
    return render_template("login.html")

# Página principal
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",
        activos=52,
        visitas=12,
        total=120
    )

if __name__ == "__main__":
    app.run(debug=True)
