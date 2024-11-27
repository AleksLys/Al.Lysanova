import requests  
import json
from pprint import pprint 

username = "spark"
url = f"https://github.com/apache/{username}"
user_data = requests.get(url).json()

print(user_data)
print('-'*25)
x = json.dumps(user_data)
user_data1 = json.loads(x)

info = {
    'company': (user_data["company"]),
    'created_at': (user_data["created_at"]),
    'email': (user_data["email"]),
    'id': (user_data["id"]),
    'name': (user_data["name"]),
    'url': (user_data["url"]),
}
print(info)

with open("filejson.txt", "w") as write_file:
    json.dump(info, write_file)
