from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


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
           
      def create_person(self, renda_mensal:float, idade:int, nome_completo:str,celular:str,categoria:str, saldo:float) -> None:
         with self.__db_connection() as database:
            try:
               person_data = PessoaFisicaTable(
                  renda_mensal=renda_mensal,
                  idade=idade,
                  nome_completo=nome_completo,
                  celular=celular,
                  categoria=categoria,
                  saldo=saldo
               )
               database.session.add(person_data)
               database.session.commit()
            except Exception as expcetion:
               database.session.rollback()
               raise expcetion

      def get_person(self, client_id: int) -> None:
         with self.__db_connection() as database:
            try:
               person = (database.session
                        .query(PessoaFisicaTable)
                        .filter(PessoaFisicaTable.id == client_id)
                        .first())
               return person
            except NoResultFound:
               return None

      def update_saldo(self, client_id: int, saldo: float) -> PessoaFisicaTable | None:
         with self.__db_connection() as database:
            try:
               person = (database.session
                        .query(PessoaFisicaTable)
                        .filter(PessoaFisicaTable.id == client_id)
                        .first())

               if person is None:
                  return None

               person.saldo = saldo
               database.session.commit()
               database.session.refresh(person)
               return person
            except Exception as exception:
               database.session.rollback()
               raise exception

      def sacar(self, client_id: int, valor: float) -> PessoaFisicaTable | None:
         with self.__db_connection() as database:
            try:
               person = (database.session
                        .query(PessoaFisicaTable)
                        .filter(PessoaFisicaTable.id == client_id)
                        .first())

               if person is None:
                  return None

               person.sacar(valor)
               database.session.commit()
               database.session.refresh(person)
               return person
            except Exception as exception:
               database.session.rollback()
               raise exception

      def extrato(self, client_id: int) -> dict | None:
         with self.__db_connection() as database:
            try:
               person = (database.session
                        .query(PessoaFisicaTable)
                        .filter(PessoaFisicaTable.id == client_id)
                        .first())

               if person is None:
                  return None

               return {
                  "account": person.extrato(),
                  "transactions": [],
               }
            except Exception as exception:
               raise exception

      
           
      
