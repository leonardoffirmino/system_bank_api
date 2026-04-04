from src.controllers.pessoa_juridica.interfaces.pessoa_juridica_controller_interface import PessoaJuridicaControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.view_interface import ViewInterface


class PessoaJuridicaListView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_people()
        return HttpResponse(status_code=200, body=body_response)
