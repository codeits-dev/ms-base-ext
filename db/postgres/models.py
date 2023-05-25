from sqlalchemy import Column, Integer, String,Date, DateTime,Boolean, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import UniqueConstraint
from sqlalchemy import event

from codeits.db.sql.connection import SqlConnection
from codeits.db.sql.util import UtilSQLAlchemy
from codeits.log.UtilLog import UtilLog

import datetime


Base = declarative_base()
metadata = Base.metadata
db = SqlConnection.getSqlAlchemy()




class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    birthdate = Column(Date, nullable=False)
    
    
    @staticmethod
    def create(**kwargs):
        return UtilSQLAlchemy.insert(Person, **kwargs)
    
    @staticmethod
    def all_persons(**kwargs):
        #return Person.query.all()
        data = UtilSQLAlchemy.list_paginable(Person,kwargs)
        return data