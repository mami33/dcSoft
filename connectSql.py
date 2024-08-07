import requests
from getmac import get_mac_address as gma
from my_configs import *
global gmaa
gmaa = gma()
def newUser(data=""):
    if data == "":
        url = 'http://77.79.80.209:5000/MyWeb/linkserver/'
        myobj = {'data': gmaa }
        try:
            x = requests.post(url, data = myobj,timeout = 3)
            return x.text
        except requests.exceptions.Timeout:
            return 'Timeout'
    else:
        url = 'http://77.79.80.209:5000/MyWeb/linkserver/update_user.php'
        myobj = {'data': data}
        try:
            x = requests.post(url, data = myobj,timeout = 3)
            return (x.text)
        except requests.exceptions.Timeout:
            return 'Timeout'

# print(newUser("numara;iban;pp;mami"))