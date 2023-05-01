import json
import os

from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")
data = json.load(
    open("./app/data/data.json")
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


@app.route("/photo")
def get_photo():
    return render_template("photo.jinja")


@app.route("/photo/mythology")
def get_photo_mythology():
    return render_template("photo-mythology.jinja")

@app.route("/photo/cemeteries")
def get_photo_cemetereis():
    return render_template("photo-cemeteries.jinja")

@app.route("/photo/fruit")
def get_photo_fruit():
    return render_template("photo-fruit.jinja")

@app.route("/photo/roommates")
def get_photo_roommates():
    return render_template("photo-roommates.jinja")


@app.errorhandler(404)
def get_error_page(error):
    return render_template("404.jinja"), 404


if __name__=="__main__":
    app.run(debug=False)
