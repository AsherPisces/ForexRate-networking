# import requests # to make GET request
# import json

# def download(url, file_name):
#     # open in binary mode
#     with open(file_name, "w") as file:
#         # get request
#         api_key_url = "https://vapi.vnappmob.com/api/request_api_key?scope=exchange_rate"
#         api_key = requests.get(api_key_url).json()["results"]
#         headers = {}
#         headers["Authorization"] = "Bearer " + api_key
#         response = requests.get(url, headers = headers)
#         # write to file
#         file.write(json.dumps(response.json()))

# download("https://vapi.vnappmob.com/api/v2/exchange_rate/vcb", "data_vietcombank.json")
# # download("https://api.exchangerate.host/timeseries?start_date=2021-01-01&end_date=2021-07-31&base=USD", "past.json")

# setData = []
# with open("data_vietcombank.json", "r") as file:
#     temp = file.read()
#     setData = json.loads(temp)['results']
# for i in setData:
#     print(i)


from requests import get  # to make GET request
from xml.dom import minidom

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

download("https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx", "data_vietcombank.xml")

my_tree = minidom.parse('data_vietcombank.xml')
tag_name = my_tree.getElementsByTagName('Exrate')
setData = [] # save Data here
header_table_data = ["Currency Code", "Currency Name", "Cash", "Transfer", "Selling Rates"]
setData.append(header_table_data)
date = my_tree.getElementsByTagName('DateTime')[0]
day = date.childNodes[0]
data_current = []
for x in tag_name:
    data_current.append(x.attributes['CurrencyCode'].value)
    data_current.append(x.attributes['CurrencyName'].value)
    data_current.append(x.attributes['Buy'].value)
    data_current.append(x.attributes['Transfer'].value)
    data_current.append(x.attributes['Sell'].value)
    setData.append(data_current)
    data_current = []

setData.append(day.nodeValue)





