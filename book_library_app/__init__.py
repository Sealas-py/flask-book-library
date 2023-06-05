from config import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.app_context().push()
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    from book_library_app.authors import authors_bp
    from book_library_app.commands import db_manage_bp
    from book_library_app.errors import errors_bp
    from book_library_app.books import books_bp
    from book_library_app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(books_bp, url_prefix='/api/v1')
    app.register_blueprint(authors_bp, url_prefix='/api/v1')
    app.register_blueprint(db_manage_bp)
    app.register_blueprint(errors_bp)

    return app
