import cgi, cgitb
import json
import os
import requests

form = cgi.FieldStorage()

wea = {
    "nombre": form.getvalue('nombre'),
    "serie_id": form.getvalue('serie'),
    "image_url": form.getvalue('image_url')
}

headers = {
    "Content-Type": "application/json"
}

requests.post("http://localhost:3000/api/waifus", data=json.dumps(wea), headers=headers)

print("Content-type:text/html\r\n\r\n")
with open("C:/Users/Coke/Desktop/wea/exitoso.html", 'r') as f:
    print(f.read())