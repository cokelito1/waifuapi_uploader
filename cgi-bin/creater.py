import cgi, cgitb
import json
import requests
import os

series = {}

with open("C:/Users/Coke/Desktop/wea/header_create_waifu.html") as f:
    print(f.read())

r_series = requests.get("http://localhost:3000/api/series")
for serie in r_series.json():
    series[serie["nombre"]] = serie["_id"]

print("<select name=\"serie\" class=\"form-control\" id=\"serie\">")
for key in series:
    print("<option value=\"" + series[key] + "\">" + key + "</option>")
print("</select>")

with open("C:/Users/Coke/Desktop/wea/footer_create_waifu.html") as f:
    print(f.read())