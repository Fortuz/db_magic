from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = Field(gt=0, lt=120)
    email: Optional[str] = None

user = User(age=25, name="Alice")

print(user)

user2 = User(name="Bob", age=-5)

print(user2.age)
print(type(user2.age))