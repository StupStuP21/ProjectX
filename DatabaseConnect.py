from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session


class DatabaseConnect():
    Driver = 'ODBC Driver 17 for SQL Server'
    # Server = 'DESKTOP-0ED7FI8\SQLEXPRESS'
    Server = 'LAPTOP-98I2O88V'
    # port = 'PORT=1433'
    Database = 'ProjectXX'
    # Database = 'AdventureWorks2019'

    Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'
    engine = create_engine(Database_con)
    Base = declarative_base()
    session = Session(bind=engine)

    def __init__(self, Driver, Server, Database):
        self.Driver = Driver
        self.Server = Server
        self.Database = Database
        self.Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'
        self.engine = create_engine(self.Database_con)
        self.Base = declarative_base()
        self.session = Session(bind=self.engine)


connect = DatabaseConnect('ODBC Driver 17 for SQL Server', 'LAPTOP-98I2O88V', 'ProjectXX')
