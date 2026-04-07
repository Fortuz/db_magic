from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session

engine = create_engine("sqlite:///db/mydatabase3.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    age = mapped_column(Integer)

Base.metadata.create_all(engine)

session = Session(engine)

session.add(User(name="Alice", age=25))
session.add(User(name="Bob", age=30))
session.commit()

users = session.query(User).all()

for user in users:
    print(user.name, user.age)