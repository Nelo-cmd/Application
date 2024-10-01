from flask import Flask

def createapp():
    app = Flask(__name__)
    app.config['SECRET KEY']= "Nelo girl"

    from views import views
    app.register_blueprint(views, url_prefix = "/")

    from auth import auth
    app.register_blueprint(auth, url_prefix = '/')


    return app 
