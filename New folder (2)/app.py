from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = "os_26"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://tl_S2403570:tl_S2403570@ND-COMPSCI/tl_s2403570_rza"
    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)
    migrate = Migrate(app, db)
    return app
