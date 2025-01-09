from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'
    
    db. init_app(app)
    
    from blueprint_app.core.routes import core
    from blueprint_app.todos.routes import todos
    from blueprint_app.people.routes import people
    
    app.register_blueprint(core, url_prefix= '/')
    app.register_blueprint(todos, url_prefix = '/todos')
    app.register_blueprint(people, url_prefix = '/people')
    
    migrate = Migrate(app,db)
    
    return app
    
    
    