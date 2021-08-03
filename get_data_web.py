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
data_current = []
for x in tag_name:
    data_current.append(x.attributes['CurrencyCode'].value)
    data_current.append(x.attributes['CurrencyName'].value)
    data_current.append(x.attributes['Buy'].value)
    data_current.append(x.attributes['Transfer'].value)
    data_current.append(x.attributes['Sell'].value)
    setData.append(data_current)
    data_current = []






