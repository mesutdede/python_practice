# -*- coding: utf-8 -*-

import json

with open("users.json") as users:
    data = json.load(users) # dosyadan okurken load
    print(data[1]["address"]["geo"]["lat"])