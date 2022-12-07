from flask import session, redirect, flash


def login_required(ruta):

    def wrapper(*args, **kwargs):
        if 'user' not in session or session['user'] is None:
            flash('Usted no tiene acceso a esta parte del sitio', 'error')
            return redirect('/auth')
        resp = ruta(*args, **kwargs)
        return resp
    
    return wrapper