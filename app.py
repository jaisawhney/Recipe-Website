from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/categories")
def show_categories():
    return render_template("categories.html")


@app.route("/recipes")
def show_recipes():
    return render_template("recipes.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5200))
