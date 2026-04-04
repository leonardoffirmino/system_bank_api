from src.controllers.pessoa_juridica.interfaces.pessoa_juridica_controller_interface import PessoaJuridicaControllerInterface
from src.validators.pessoa_juridica_validator import pessoa_juridica_statement_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.view_interface import ViewInterface


class PessoaJuridicaStatementView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_statement_validator(http_request)

        client_id = http_request.params["id"]
        body_response = self.__controller.extrato(client_id)

        return HttpResponse(status_code=200, body=body_response)
