from src.controllers.pessoa_fisica.interfaces.pessoa_fisica_controller_interface import PessoaFisicaControllerInterface
from src.validators.pessoa_fisica_validator import pessoa_fisica_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.view_interface import ViewInterface


class PessoaFisicaCreatorView(ViewInterface):
    def __init__(self, controller: PessoaFisicaControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_creator_validator(http_request)

        person_info = http_request.body
        body_response = self.__controller.create_person(
            person_info["renda_mensal"],
            person_info["idade"],
            person_info["nome_completo"],
            person_info["celular"],
            person_info["categoria"],
            person_info["saldo"],
        )

        return HttpResponse(status_code=201, body=body_response)
