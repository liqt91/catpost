from flask import Blueprint, render_template

test = Blueprint('test', __name__)


@test.route('/')
def _test():
    return render_template('base.html')
