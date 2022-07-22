import json

data = '{"name":"Tirth","Age":"21","City":"Ahmedabad"}'
print(data)
# print(data['name'])  <-- throws an error

parsed = json.loads(data)
print(parsed)
print(parsed['name'])

jsonD = json.dumps(parsed)
print(jsonD)
