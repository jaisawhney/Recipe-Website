from flask import Flask, render_template, redirect, url_for, request
import os
import json

file = open("mock-data.json")
mock_data = json.load(file)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/categories")
def show_categories():
    categories = mock_data["categories"]
    return render_template("categories.html", categories=categories)


@app.route("/recipes")
def show_recipes():
    category = request.args.get("category") or None
    recipes = mock_data["recipes"]
    return render_template("recipes.html", recipes=recipes, category=category, categories=mock_data["categories"])


@app.route("/recipes/<string:recipe_id>")
def show_recipe(recipe_id):
    recipe = next(recipe for recipe in mock_data["recipes"] if recipe["id"] == recipe_id)
    if recipe:
        return render_template("recipe.html", recipe=recipe)
    else:
        return redirect(url_for("show_recipes"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5200))
