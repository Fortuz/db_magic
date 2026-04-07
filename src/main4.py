from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Session

engine = create_engine("sqlite:///db/mydatabase4.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)

    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"

    id = mapped_column(Integer, primary_key=True)
    product = mapped_column(String)

    user_id = mapped_column(ForeignKey("users.id"))

    user = relationship("User", back_populates="orders")

Base.metadata.create_all(engine)

session = Session(engine)

alice = User(name="Alice")
alice.orders.append(Order(product="Laptop"))
alice.orders.append(Order(product="Mouse"))

session.add(alice)
session.commit()

user = session.query(User).first()

for order in user.orders:
    print(order.product)