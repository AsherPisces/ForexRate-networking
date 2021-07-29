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
data_current = {}
for x in tag_name:
    data_current['CurrencyCode'] = x.attributes['CurrencyCode'].value
    data_current['CurrencyName'] = x.attributes['CurrencyName'].value
    data_current['Buy'] = x.attributes['Buy'].value
    data_current['Transfer'] = x.attributes['Transfer'].value
    data_current['Sell'] = x.attributes['Sell'].value
    setData.append(data_current)
    data_current = {}







