from sqlalchemy.exc import NoResultFound
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):
      def __init__(self,db_connection) -> None:
          self.__db_connection = db_connection

      def list_people(self) -> list[PessoaJuridicaTable]:
           with self.__db_connection() as database:
              try:
                 people = database.session.query(PessoaJuridicaTable).all()
                 return people
              except NoResultFound:
                 return []
              
      def create_person(self,razao_social:str, nome_fantasia:str, cnpj:str, email:str, limit_saque:float) -> None:
          with self.__db_connection() as database:
              try:
                person_data = PessoaJuridicaTable(
                    razao_social=razao_social,
                    nome_fantasia=nome_fantasia,
                    cnpj=cnpj,
                    email=email,
                    limit_saque=limit_saque
                )
                database.session.add(person_data)
                database.session.commit()
              except Exception as exception:
                database.session.rollback()
                raise exception 
                  
      def get_person(self,cliente_id: int) -> PessoaJuridicaTable | None:
          with self.__db_connection() as database:
              try:
                  person = database.session.query(PessoaJuridicaTable).filter(PessoaJuridicaTable.id == cliente_id).first()
                  return person
              except NoResultFound:
                  return None

      def update_saldo(self,cliente_id: int, novo_saldo: float) -> PessoaJuridicaTable | None:
          with self.__db_connection() as database:
              try:
                  person = self.get_person(cliente_id)
                  if person:
                      person.saldo = novo_saldo
                      database.session.commit()
                  return person
              except Exception as exception:
                  database.session.rollback()
                  raise exception