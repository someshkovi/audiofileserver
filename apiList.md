


GET: http://127.0.0.1:8000/podcasts/65465561/


import requests

url = "http://127.0.0.1:8000/podcasts/8749874894/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


curl --location --request GET 'http://127.0.0.1:8000/podcasts/8749874894/' --data-raw ''


DELETE: http://127.0.0.1:8000/podcasts/65465561/

curl --location --request DELETE 'http://127.0.0.1:8000/podcasts/8749874894/' \
--data-raw ''

import requests

url = "http://127.0.0.1:8000/podcasts/8749874894/"

payload={}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)



PUT(UPDATE): http://127.0.0.1:8000/podcasts/65465561/

import requests

url = "http://127.0.0.1:8000/podcasts/65465561/"

payload="{\r\n    \"id\": 65465561,\r\n    \"name\": \"joe rogan 2021\",\r\n    \"created_at\": \"2021-03-10T13:44:00Z\"\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)


curl --location --request PUT 'http://127.0.0.1:8000/podcasts/65465561/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": 65465561,
    "name": "joe rogan 2021",
    "created_at": "2021-03-10T13:44:00Z"
}'

POST: http://127.0.0.1:8000/podcasts/

curl --location --request POST 'http://127.0.0.1:8000/podcasts/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": 46555664,
    "name": "tester",
    "created_at": "2021-03-10T14:39:00Z"
}'

import requests

url = "http://127.0.0.1:8000/podcasts/"

payload={'id': '1236',
'name': 'docker',
'created_at': '2021-03-10T14:39:00Z'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
