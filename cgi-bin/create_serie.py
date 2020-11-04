import cgi, cgitb
import json
import os
import requests

form = cgi.FieldStorage()

wea = {
    "nombre": form.getvalue('nombre'),
    "cantidad_capitulos": int(form.getvalue('cap')),
}
headers = {"Content-Type": "application/json"}

print("Content-type:text/html\r\n\r\n")
try:
    requests.post("http://localhost:3000/api/series", data=json.dumps(wea), headers=headers)
except:
    print("<h1> what wea </h1>")
finally:
    with open("C:/Users/Coke/Desktop/wea/exitoso.html", 'r') as f:
        print(f.read())