from flask import Blueprint, jsonify, request

from src.main.composer.pessoa_fisica_composer import (
    pessoa_fisica_creator_view,
    pessoa_fisica_finder_view,
    pessoa_fisica_list_view,
    pessoa_fisica_saldo_updater_view,
    pessoa_fisica_statement_view,
    pessoa_fisica_withdraw_view,
)
from src.views.http_types.http_request import HttpRequest

pessoa_fisica_route_bp = Blueprint("pessoa_fisica", __name__, url_prefix="/pessoa_fisica")

@pessoa_fisica_route_bp.route("/", methods=["GET"])
def list_people():
    http_request = HttpRequest(method="GET")
    http_response = pessoa_fisica_list_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/", methods=["POST"])
def create_person():
    http_request = HttpRequest(body=request.get_json(), method="POST")
    http_response = pessoa_fisica_creator_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/<int:id>", methods=["GET"])
def get_person(id: int):
    http_request = HttpRequest(method="GET", params={"id": id})
    http_response = pessoa_fisica_finder_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/<int:id>/saldo", methods=["PATCH"])
def update_saldo(id: int):
    http_request = HttpRequest(body=request.get_json(), method="PATCH", params={"id": id})
    http_response = pessoa_fisica_saldo_updater_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/<int:id>/sacar", methods=["POST"])
def withdraw(id: int):
    http_request = HttpRequest(body=request.get_json(), method="POST", params={"id": id})
    http_response = pessoa_fisica_withdraw_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/<int:id>/extrato", methods=["GET"])
def statement(id: int):
    http_request = HttpRequest(method="GET", params={"id": id})
    http_response = pessoa_fisica_statement_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
