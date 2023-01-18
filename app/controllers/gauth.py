from flask import request, redirect, render_template, Blueprint, flash, session
from app.models.users import User
from app.decorators import login_required

gauth = Blueprint('gauth', __name__, template_folder='templates')


@gauth.route('/gauth')
def begin():
    return 'Controlaor de Google Auth'


@gauth.route('/gauth/private')
@login_required
def private():
    return 'Ruta privada'
