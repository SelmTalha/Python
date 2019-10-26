
person='{"name":"Selim","languages":["Python","C#","Java"]}' #Json Stringi

print(type(person))

import json 

result=json.loads(person) # loads: str classlı personu dicte dönüştürüldü.
print(type(result))
print(result["name"])
print(result["languages"])

with open("person.json") as f:
    data=json.load(f)
    print(data["name"])
    print(data["surname"])
    print(data["age"])

person={
    "name":"Selim",
    "languages":["Python","C#","Java"]
    }
print(type(person))
result=json.dumps(person)
print(type(result))
print(repr(result))
