import requests
from datetime import  datetime

USERNAME = 'daivik'
TOKEN = 'daivikpixela'

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_params= {
    'id':'graph1',
    'name':'Cycling Graph',
    'unit':'Km',
    'type':'float',
    'color':'ajisai'

}

headers={
    'X-USER-TOKEN':TOKEN
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'
pixel_data = {
    'date':datetime(year=2021,month=3,day=29).strftime('%Y%m%d'),
    'quantity':'15',

}

response =requests.post(pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)
