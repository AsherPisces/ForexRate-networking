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
data = my_tree.getElementsByTagName('Exrate')[0]
print(data.attributes['CurrencyCode'].value)

tag_name = my_tree.getElementsByTagName('Exrate')

# print(CurrencyCode_att[0].value)

setData = [] # save Data here
CurrencyCode = []
CurrencyName = []
Buy = []
Transfer = []
Sell = []
for x in tag_name:
    CurrencyCode.append(x.attributes['CurrencyCode'].value)
    CurrencyName.append(x.attributes['CurrencyName'].value)
    Buy.append(x.attributes['Buy'].value)
    Transfer.append(x.attributes['Transfer'].value)
    Sell.append(x.attributes['Sell'].value)
setData.append(CurrencyCode)
setData.append(CurrencyName)
setData.append(Buy)
setData.append(Transfer)
setData.append(Sell)


print(setData)






