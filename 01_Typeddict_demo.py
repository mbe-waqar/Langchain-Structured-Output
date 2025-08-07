from typing import TypedDict

class person(TypedDict):
    name: str
    age: int

new_person: person = {"name": "John", "age": 30}

print(new_person)
print(new_person["name"])
print(new_person["age"])