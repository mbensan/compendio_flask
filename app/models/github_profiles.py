from flask import flash
from app.models.connection import connectToMySQL 

create_table = '''
create table if not exists github_profile  (
    id int auto_increment primary key,
    name varchar(100),
    login varchar(255),
    followers int not null default 0,
    following int not null default 0,
    public_repos int not null default 0,
    public_gists int not null default 0,
    total int not null default 0
)
'''
connectToMySQL().query_db(create_table)


class GithubProfile:

    def __init__(self):
        pass
    
    @classmethod
    def create(cls, name, login, public_repos, public_gists, followers, following, total):
        query = '''
            insert into github_profile 
            (name, login, public_repos, public_gists, followers, following, total) 
            values (%(name)s, %(login)s, %(public_repos)s, %(public_gists)s, %(followers)s, %(following)s, %(total)s)
        '''
        
        data = {
            'name': name,
            'login': login,
            'public_repos': int(public_repos),
            'public_gists': int(public_gists),
            'followers': int(followers),
            'following': int(following),
            'total': int(total)
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        new_profile_id = connectToMySQL().query_db(query, data)

        # retornamos el ID del usuario recientemente creado
        return new_profile_id

    @classmethod
    def get_all(cls):
        query = 'select * from github_profile'

        response = connectToMySQL().query_db(query)

        return response