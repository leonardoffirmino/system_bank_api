from flask import Blueprint, jsonify, request
from src.main.composer.pessoa_juridica_composer import (
    pessoa_juridica_creator_view,
    pessoa_juridica_finder_view,
    pessoa_juridica_list_view,
    pessoa_juridica_saldo_updater_view,
    pessoa_juridica_statement_view,
    pessoa_juridica_withdraw_view,
)
from src.views.http_types.http_request import HttpRequest

pessoa_juridica_route_bp = Blueprint("pessoa_juridica", __name__, url_prefix="/pessoa_juridica")

@pessoa_juridica_route_bp.route("/", methods=["GET"])
def list_people():
    http_request = HttpRequest(method="GET")
    http_response = pessoa_juridica_list_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/", methods=["POST"])
def create_person():
    http_request = HttpRequest(body=request.get_json(), method="POST")
    http_response = pessoa_juridica_creator_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/<int:id>", methods=["GET"])
def get_person(id: int):
    http_request = HttpRequest(method="GET", params={"id": id})
    http_response = pessoa_juridica_finder_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/<int:id>/saldo", methods=["PATCH"])
def update_saldo(id: int):
    http_request = HttpRequest(body=request.get_json(), method="PATCH", params={"id": id})
    http_response = pessoa_juridica_saldo_updater_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/<int:id>/sacar", methods=["POST"])
def withdraw(id: int):
    http_request = HttpRequest(body=request.get_json(), method="POST", params={"id": id})
    http_response = pessoa_juridica_withdraw_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/<int:id>/extrato", methods=["GET"])
def statement(id: int):
    http_request = HttpRequest(method="GET", params={"id": id})
    http_response = pessoa_juridica_statement_view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
