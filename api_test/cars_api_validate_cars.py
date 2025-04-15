import requests
my_session = requests.Session()

base_url = "http://127.0.0.1:5000/"
username = "qxf2"
password = "qxf2"

response = my_session.get(url=base_url + 'cars',auth=(username,password))
cars_before_add = response.json()
print(f'cars present before adding the car:{cars_before_add}')

response = my_session.post(url=base_url + 'cars/add',json={'name':'gwagon','brand':'Gwagon','price_range':'90-20 lacs','car_type':'sedan'},auth=(username,password))
# print(response.status_code)
assert response.status_code==200

response = my_session.get(url=base_url + 'cars',auth=(username,password))
cars_after_add = response.json()
print(f"cars after adding the car:{cars_after_add}")