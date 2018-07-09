# coding: utf-8
from flask import session

from models.user import User


def current_user():
    uid = session.get('user_id', -1)
    u = User.find_by(id=int(uid))
    return u