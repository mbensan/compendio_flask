import json
from flask import request, redirect, render_template, Blueprint, flash, session
from app.models.github_profiles import GithubProfile 
github_ajax = Blueprint('github_ajax', __name__, template_folder='templates')


# rutas nuevas
@github_ajax.route('/ajax/github')
def get_github_profiles():
    profiles = GithubProfile.get_all()
    return json.dumps(profiles)


@github_ajax.route('/ajax/github', methods=['POST'])
def add_github_user():
    id = GithubProfile.create(
        request.form['name'],
        request.form['login'],
        request.form['public_repos'],
        request.form['public_gists'],
        request.form['followers'],
        request.form['following'],
        request.form['total'],
    )
    return '{"id": ' + str(id) + '}'
