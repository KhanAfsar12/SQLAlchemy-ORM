from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from models import User, engine
from sqlalchemy import or_, and_, not_, func, Column, Integer, String, ForeignKey, create_engine

db_url = 'sqlite:///database.db'
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__  = True
    id = Column(Integer, primary_key=True)    

class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    user_id = Column(ForeignKey("users.id"))

    def __repr__(self):
        return f"<Address(id={self.id}, city={self.city})>"

class User(BaseModel):
    __tablename__ = "users"
    name = Column(String)
    age = Column(Integer)
    addresses = relationship(Address)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.name})>"

Base.metadata.create_all(engine)