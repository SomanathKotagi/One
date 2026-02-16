import json
data={
    'name':'Somanath',
    'age':25,
}
json_str=json.dumps(data)
print(json_str)

print(type(json_str))

passed_data=json.loads(json_str)
print(passed_data)
print(type(passed_data))

