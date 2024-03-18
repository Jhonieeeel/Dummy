from flask import Flask, render_template, send_from_directory


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/admin")
def admin():
    return render_template("admin-page.html")

@app.route("/login")
def login():
    return render_template("admin-login.html")

@app.route("/preline.js")
def serve_preline_js():
    return send_from_directory("node_modules/preline/dist", "preline.js")


if __name__ == "__main__":
    app.run(debug=True)