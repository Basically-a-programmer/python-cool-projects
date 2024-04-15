import requests
import datetime

username = "shivamsingh"
token = "letsfindthecode"

pixela_param = {
    'token': "letsfindthecode",
    'username': "shivamsingh",
    'agreeTermsOfService':"yes",
    'notMinor':  "yes",
}
pixela_endpoint = "https://pixe.la/v1/users"
# the act is created
# request = requests.post(pixela_endpoint,json=pixela_param)
# print(request.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_param = {
    'id':"graph1",
    'name':"cycling graph",
    'unit': 'km',
    'type': 'int',
    'color': 'shibafu'

}
header = {
    "X-USER-TOKEN":token
}

request = requests.post(graph_endpoint,json=graph_param,headers=header)

grap1_endpoint = f"{graph_endpoint}/graph1"
today = datetime.datetime(year=2023,month=11,day=27)
graph1_param = {
    'date':today.strftime("%Y%m%d"),
    'quantity':"3",
}

graph1_request = requests.post(url=grap1_endpoint,json=graph1_param,headers=header)
print(graph1_request)

change_endpoint = f"{grap1_endpoint}/{today.strftime('%Y%m%d')}"

change_para = {
    'quantity':'15'
}
change_request = requests.put(url=change_endpoint,json=change_para,headers=header)
print(change_request)