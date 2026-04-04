from src.controllers.pessoa_fisica.interfaces.pessoa_fisica_controller_interface import PessoaFisicaControllerInterface
from src.validators.pessoa_fisica_validator import pessoa_fisica_finder_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.view_interface import ViewInterface


class PessoaFisicaFinderView(ViewInterface):
    def __init__(self, controller: PessoaFisicaControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_finder_validator(http_request)

        client_id = http_request.params["id"]
        body_response = self.__controller.get_person(client_id)

        return HttpResponse(status_code=200, body=body_response)
