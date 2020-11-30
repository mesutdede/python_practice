# -*- coding: utf-8 -*-

import json

data = '{"firstName": "mesut", "lastName": "dede"}'

jsonData = json.loads(data) # string den json data olusturur.

print(type(jsonData))

print(jsonData["firstName"])
print(jsonData["lastName"])


customer = {
        "firstName": "cem",
        "lastName": "yilmaz"
    }

customerJson = json.dumps(customer) # python objesinden json data olusturur.

print(customerJson)