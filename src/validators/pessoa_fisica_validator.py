from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_request import HttpRequest


def validate_create_payload(payload: dict) -> None:
    if not isinstance(payload, dict):
        raise HttpBadRequestError("Payload invalido")

    required = ["renda_mensal", "idade", "nome_completo", "celular", "categoria", "saldo"]
    for key in required:
        if key not in payload:
            raise HttpBadRequestError(f"Campo obrigatorio ausente: {key}")

    if payload["renda_mensal"] < 0:
        raise HttpBadRequestError("renda_mensal deve ser nao-negativa")
    if payload["idade"] <= 0:
        raise HttpBadRequestError("idade deve ser positiva")
    if not isinstance(payload["nome_completo"], str) or not payload["nome_completo"].strip():
        raise HttpBadRequestError("nome_completo invalido")
    if payload["saldo"] < 0:
        raise HttpBadRequestError("saldo deve ser nao-negativo")


def validate_client_id(client_id: int) -> None:
    if client_id is None or not isinstance(client_id, int) or client_id <= 0:
        raise HttpBadRequestError("client_id deve ser inteiro positivo")


validate_id = validate_client_id


def pessoa_fisica_creator_validator(http_request: HttpRequest) -> None:
    validate_create_payload(http_request.body)


def pessoa_fisica_finder_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))


def pessoa_fisica_saldo_updater_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))

    if not isinstance(http_request.body, dict):
        raise HttpBadRequestError("Payload invalido")

    if "saldo" not in http_request.body:
        raise HttpBadRequestError("campo 'saldo' ausente")

    saldo = http_request.body["saldo"]
    if saldo is None or not isinstance(saldo, (int, float)):
        raise HttpBadRequestError("saldo deve ser um numero")


def pessoa_fisica_withdraw_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))

    if not isinstance(http_request.body, dict):
        raise HttpBadRequestError("Payload invalido")

    if "valor" not in http_request.body:
        raise HttpBadRequestError("campo 'valor' ausente")

    valor = http_request.body["valor"]
    if valor is None or not isinstance(valor, (int, float)):
        raise HttpBadRequestError("valor deve ser um numero")


def pessoa_fisica_statement_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))
