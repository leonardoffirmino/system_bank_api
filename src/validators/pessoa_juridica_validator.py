from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_request import HttpRequest


def validate_create_payload(payload: dict) -> None:
    if not isinstance(payload, dict):
        raise HttpBadRequestError("Payload invalido")

    required = ["razao_social", "nome_fantasia", "cnpj", "email", "limit_saque"]
    for key in required:
        if key not in payload:
            raise HttpBadRequestError(f"Campo obrigatorio ausente: {key}")

    if not isinstance(payload["razao_social"], str) or not payload["razao_social"].strip():
        raise HttpBadRequestError("razao_social invalido")
    if not isinstance(payload["cnpj"], str) or not payload["cnpj"].strip():
        raise HttpBadRequestError("cnpj invalido")
    if payload["limit_saque"] is None or payload["limit_saque"] < 0:
        raise HttpBadRequestError("limit_saque deve ser nao-negativo")


def validate_client_id(client_id: int) -> None:
    if client_id is None or not isinstance(client_id, int) or client_id <= 0:
        raise HttpBadRequestError("client_id deve ser inteiro positivo")


validate_id = validate_client_id


def pessoa_juridica_creator_validator(http_request: HttpRequest) -> None:
    validate_create_payload(http_request.body)


def pessoa_juridica_finder_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))


def pessoa_juridica_saldo_updater_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))

    if not isinstance(http_request.body, dict):
        raise HttpBadRequestError("Payload invalido")

    if "saldo" not in http_request.body:
        raise HttpBadRequestError("campo 'saldo' ausente")

    saldo = http_request.body["saldo"]
    if saldo is None or not isinstance(saldo, (int, float)):
        raise HttpBadRequestError("saldo deve ser um numero")


def pessoa_juridica_withdraw_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))

    if not isinstance(http_request.body, dict):
        raise HttpBadRequestError("Payload invalido")

    if "valor" not in http_request.body:
        raise HttpBadRequestError("campo 'valor' ausente")

    valor = http_request.body["valor"]
    if valor is None or not isinstance(valor, (int, float)):
        raise HttpBadRequestError("valor deve ser um numero")


def pessoa_juridica_statement_validator(http_request: HttpRequest) -> None:
    validate_client_id(http_request.params.get("id"))
