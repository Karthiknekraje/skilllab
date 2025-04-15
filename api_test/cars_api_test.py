import requests

response = requests.get("http://127.0.0.1:5000/cars", auth=("qxf2","qxf2"))

print(response.status_code)

response_content = response.json()
print(response_content)