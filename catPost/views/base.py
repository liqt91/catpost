from flask import Blueprint, render_template

base = Blueprint('base', __name__)


@base.route('/')
def _base():
    return render_template('base.html')
