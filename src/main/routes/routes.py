from flask import Flask
from src.main.routes.pessoa_fisica_routes import pessoa_fisica_route_bp
from src.main.routes.pessoa_juridica_routes import pessoa_juridica_route_bp


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(pessoa_fisica_route_bp)
    app.register_blueprint(pessoa_juridica_route_bp)
