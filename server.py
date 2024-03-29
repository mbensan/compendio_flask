from app import app

# registramos los controladores de la app
from app.controllers.auth import auth
from app.controllers.pages import pages
from app.controllers.github_ajax import github_ajax
from app.controllers.gauth import gauth

app.register_blueprint(auth)
app.register_blueprint(pages)
app.register_blueprint(github_ajax)
app.register_blueprint(gauth)
'''
from app.controllers.azar import azar
from app.controllers.twitter import twitter
from app.controllers.books import books

app.register_blueprint(azar)
app.register_blueprint(twitter, url_prefix='/twitter')
app.register_blueprint(books, url_prefix='/books')

'''
if __name__=="__main__":   
    app.run(debug=True)    
