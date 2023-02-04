people= [
    {"name":"harry","house":"gryfindor"},
    {"name":"cho","house":"ravenclaw"},
    {"name": "draco","house":"slytherin"}
]
def f(person):
    return person["name"]

people.sort(key=f)
print(people)