import requests
from datetime import datetime

USERNAME = "" # your username
TOKEN = "" # your token
GRAPH_ID = "" # your name for graph ID

# ----------------------------------------------------------------------------------------------

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# ----------------------------------------------------------------------------------------------

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",
}

# ----------------------------------------------------------------------------------------------

today = datetime.now()

response1 = requests.post(url=pixela_endpoint, json=user_parameters) # comment this row once you create your account or you will receive an error
response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers) # comment this row once you create your account or you will receive an error
response3 = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)

print(response1.text)
print(response2.text)
print(response3.text)

