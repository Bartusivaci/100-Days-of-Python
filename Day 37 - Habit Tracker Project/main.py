import requests
from datetime import datetime

# my link to check https://pixe.la/v1/users/bartusivaci/graphs/graph1.html

USERNAME = "bartusivaci"
TOKEN = "61zwnEvjrC3VZ"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you walk today?: "),
}

# create a pixel
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": input("What is the new value?: "),
}

# update the value of a pixel
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

# delete a pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
