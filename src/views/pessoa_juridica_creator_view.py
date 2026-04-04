from src.controllers.pessoa_juridica.interfaces.pessoa_juridica_controller_interface import PessoaJuridicaControllerInterface
from src.validators.pessoa_juridica_validator import pessoa_juridica_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.view_interface import ViewInterface


class PessoaJuridicaCreatorView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_creator_validator(http_request)

        person_info = http_request.body
        body_response = self.__controller.create_person(
            person_info["razao_social"],
            person_info["nome_fantasia"],
            person_info["cnpj"],
            person_info["email"],
            person_info["limit_saque"],
        )

        return HttpResponse(status_code=201, body=body_response)
