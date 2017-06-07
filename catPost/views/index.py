from flask import Blueprint, render_template, url_for

index = Blueprint('index', __name__)


@index.route('/')
def _index():
    template = render_template("index/index.html", nav="home")
    return template


