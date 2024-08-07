from urllib.request import urlopen
from my_configs import *

import json
url = "http://77.79.80.209:5000/MyWeb/linkserver/mylinks.php"


def updateLinks():

    try:
        response = urlopen(url,timeout=3)
        data_json = json.loads(response.read())
        res = data_json["whatsAppLinks"]
        ver = data_json["version"]
        if config_get("version","ver") != ver:
            for index in res:
                 config_write("whatsAppLinks",index,res[index])
            config_write("version","ver",ver)
            return "En güncel sürüme yükseltildi"
        else:
            return "Zaten en güncel sürümü kullanıyorsunuz"


    except Exception as e:
        return "Güncelleme hatası: " + str(e)


