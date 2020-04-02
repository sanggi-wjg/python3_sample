from abc import ABC, abstractmethod


class DBManager(ABC):
    @abstractmethod
    def connection(self):
        pass


class SqlServer(DBManager):
    def connection(self):
        return 'MicroSoft Database Connected.'


class Oracle(DBManager):
    def connection(self):
        return 'Oracle Database Connected.'


class MariaDB(DBManager):
    def connection(self):
        return 'Maria Database Connected.'


class DbConnFactory:
    def get_db_connection(self, db):
        return db.connection()


if __name__ == '__main__':
    db_fact = DbConnFactory()

    print(db_fact.get_db_connection(SqlServer()))
    print(db_fact.get_db_connection(Oracle()))
    print(db_fact.get_db_connection(MariaDB()))
