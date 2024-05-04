from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:password@localhost:5432/dbname')

Base = declarative_base()

# Definindo uma classe modelo
class Exemplo(Base):
    __tablename__ = 'exemplo'
    id = Column(Integer, primary_key=True)
    campo = Column(String)

# Criando as tabelas
Base.metadata.create_all(engine)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Exemplo de inserção
exemplo = Exemplo(campo='valor')
session.add(exemplo)
session.commit()

