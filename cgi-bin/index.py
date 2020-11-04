import cgi, cgitb
import json
import requests
import os

print("Content-type:text/html\r\n\r\n")

with open("C:/Users/Coke/Desktop/wea/header_index.html") as f:
    print(f.read())

waifus_r = requests.get("http://localhost:3000/api/waifus")
waifus = waifus_r.json()
for waifu in waifus:
    try:
        print("<a href=\"#\" class=\"list-group-item\" style=\"color: black\">" + waifu["nombre"] + "<img src=\"" + waifu["image_url"] + "\" width=\"256\" height=\"256\" style=\"float: right\"></a>")
    except:
        continue

with open("C:/Users/Coke/Desktop/wea/footer_index.html") as f:
    print(f.read())
