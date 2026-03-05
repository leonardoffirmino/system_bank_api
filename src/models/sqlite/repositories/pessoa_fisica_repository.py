from sqlalchemy.orm import NoResultFound
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface

class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
      def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

      def list_people(self) -> list[PessoaFisicaTable]:
        with self.__db_connection() as database:
           try:
              people = database.session.query(PessoaFisicaTable).all()
              return people
           except NoResultFound:
              return []
           
      def create_person(self, renda_mensal:float, age:int, name:str,phone:str,category:str, balance:float):
         pass
           
      