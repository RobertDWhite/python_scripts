import requests
import json
from collections import defaultdict

url = "YOUR_SNIPE-IT_URL_HERE"
tokenMosyle = "YOUR_API_TOKEN_HERE"
assetsBearer = "Bearer YOUR_API_TOKEN_HERE"

###MOSYLE API Info###
urlMosyle = "https://businessapi.mosyle.com/v1/devices"
headersMosyle = {
    "Content-Type": "application/x-www-form-urlencoded",
    "accesstoken": f'{tokenMosyle}'
}
jsonMosyle = {
        "operation": "list",
        "options": {
            "os": "mac"
        }
    }
##Add or update the payloads below with your DB info and data
payloadFields = {
    "_snipeit_mdm_8": "Bound",
    "_snipeit_mdm_type_9": "Mosyle"
}
###SNIPE-IT API Info###
urlAssets = f'{url}/api/v1/hardware'
headersAssets = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f'{assetsBearer}'
}

rMosyle = requests.request(method="POST", url=urlMosyle, headers=headersMosyle, json=jsonMosyle)

response_dict_mosyle = rMosyle.json()
for deviceM in response_dict_mosyle["response"][0]["devices"]:
    serialMosyle = (deviceM['serial_number'])
    print(serialMosyle)
    urlAssetsCustom = f'{url}/api/v1/hardware/byserial/{serialMosyle}'
    urlFieldsGet = f'{url}/api/v1/fields'
    print(urlAssetsCustom)
    rAssetsCust = requests.request("GET", urlAssetsCustom, headers=headersAssets, verify=False)
#    print(rAssetsCust.text)
    print(rAssetsCust.json)
    response_dict_assets_cust = rAssetsCust.json()
    for deviceC in response_dict_assets_cust["rows"]:
        print("------------------------------")
        assetsID = (deviceC['id'])
        urlAssetsFields = f'{url}/api/v1/hardware/{assetsID}'
        print(urlAssetsFields)
        rAssetsFields = requests.request("PUT", urlAssetsFields, json=payloadFields, headers=headersAssets, verify=False)
        print(rAssetsFields.text)

    print("------------------------------")
    print("------------------------------")
    print("------------------------------")

print("------------------------------")
print("------------------------------")
print("------------------------------")
