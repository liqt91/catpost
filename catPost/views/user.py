from flask import Blueprint, request

from catPost.extensions import db

user = Blueprint('user', __name__)


@user.route('/register/', methods=['GET','POST'])
def userRegister():
    from catPost.models import catpost as cp
    # new_user = cp.User(username="liqt", avator=url_for('static', filename='img/avators/liqt.png'))
    # result = db.session.add(new_user)
    # db.session.commit()
    # print
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass