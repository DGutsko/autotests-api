import json

#Загрузка JSON (парсинг)

#json_data = '{"name": "Иван", "age": 30, "is_student": false}'
#parsed_data = json.loads(json_data)
#print(parsed_data["name"])
#print(parsed_data)
#print(type(parsed_data))

#Сохранение JSON (сериализация)

#data = {
    #"name": "Мария",
    #"age": 25,
    #"is_student": True
#}

#json_string = json.dumps(data, indent=4)  # Преобразуем Python-объект в JSON-строку
#print(json_string)

json_string = '{"name": "Alice", "age": 30, "is_admin": false}'
json_parced = json.loads(json_string)
print(json_parced)
print(type(json_parced))
print(json_parced["name"])

data_string = {"id": 101, "tags": ["qa", "api", "json"], "active": True}
json_data = json.dumps(data_string, indent=4)
print(json_data)


data_2 = {
  "user": "Bob",
  "roles": ["tester", "editor"]
}
with open("data_2.json", "w", encoding="utf-8") as f:
    json.dump(data_2, f, indent=2, ensure_ascii=False)


# Читаем из файла data.json
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data)



raw_json = '[{"name": "Test1"}, {"name": "Test2"}, {"name": "Test3"}]'

# 1. Преобразуем в список
data = json.loads(raw_json)

# 2. Добавим новый элемент
data.append({"name": "Test4"})

# 3. Преобразуем обратно в JSON
result_json = json.dumps(data, indent=2)

# 4. Запишем в файл
with open("tests.json", "w", encoding="utf-8") as f:
    f.write(result_json)