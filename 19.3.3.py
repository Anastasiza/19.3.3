import requests

status = 'available'

# Создание айди питомца
neebodu = '{"id": 0,"category": {"id": 0,"name": "string"},"name": "piska","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}'

pet_id = requests.post(f'https://petstore.swagger.io/v2/pet', data=neebodu, headers={"Content-Type": "application/json", 'accept': 'application/json'})
print(pet_id.json())
id = pet_id.json()['id']

# Изменение имени питомца
nebody = '{"id": ' + str(id) + ',"category": {"id": 0,"name": "string"},"name": "nepiska","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}'
put = requests.put(f'https://petstore.swagger.io/v2/pet', data=nebody, headers={"Content-Type": "application/json", 'accept': 'application/json'})
print(put.json())

# Поиск питомца по статусу
res = requests.get(f'http://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                   headers={'accept': 'application/json'})
print(res.json())
# Поиск по айди питомца.
pet = requests.get(f'https://petstore.swagger.io/v2/pet/{id}')
print(pet.json())

# Изменение статуса питомца.
body = {'name': 'Немуха', 'status': 'sold'}
post = requests.post(f'https://petstore.swagger.io/v2/pet/{id}', data=body)
print(post.json())

# Размещение заказа питомца на сайте.
bodi = '{"id": 0,"petId": '+ str(id) +',"quantity": 0,"shipDate": "2022-11-12T14:11:09.444Z","status": "placed","complete": "true"}'
store = requests.post(f'https://petstore.swagger.io/v2/store/order', data=bodi, headers={"Content-Type": "application/json", 'accept': 'application/json'})
print(store.json())
ordid = store.json()['id']

# Покупка питомца.
ord = requests.get(f'https://petstore.swagger.io/v2/store/order/{ordid}')
print(ord.json())

# Удаление покупки.
orddel = requests.delete(f'https://petstore.swagger.io/v2/store/order/{ordid}')
print(orddel.json())

# Пересчет статуса питомцев
inven = requests.get(f'https://petstore.swagger.io/v2/store/inventory')
print(inven.json())

# Удаление питомца.
deli = requests.delete(f'https://petstore.swagger.io/v2/pet/{id}')
print(deli.json())