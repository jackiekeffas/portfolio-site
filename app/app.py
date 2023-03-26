import json
import os

from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")
data = json.load(
    open("./app/data/data.json")
)


@app.route("/")
def get_home():
    return render_template("home.Jinja", projectData=data)


@app.route("/projects/<projectName>")
def get_project(projectName: str):
    return render_template(f"{projectName}.Jinja", projectData=data[projectName])


@app.route("/about")
def get_about():
    return render_template("about.Jinja")


@app.errorhandler(404)
def get_error_page(error):
    return render_template("404.Jinja"), 404

if __name__=="__main__":
    app.run(debug=False)
