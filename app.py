import json
import os

from flask import Flask, render_template


app = Flask(__name__, template_folder="/templates")
data = json.load(
    open("./data/data.json")
)


@app.route("/")
def get_home():
    return render_template("home.jinja", projectData=data)


@app.route("/projects/<projectName>")
def get_project(projectName: str):
    return render_template(f"{projectName}.jinja", projectData=data[projectName])


@app.route("/about")
def get_about():
    return render_template("about.jinja")


@app.errorhandler(404)
def get_error_page(error):
    return render_template("404.jinja"), 404

if __name__=="__main__":
    app.run(debug=False)
