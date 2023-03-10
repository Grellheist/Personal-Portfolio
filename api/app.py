from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/download_cv")
def download():
    return send_file("cv/curriculo.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run()
