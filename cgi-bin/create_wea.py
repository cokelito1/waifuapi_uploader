import cgi, cgitb
import json
import os

form = cgi.FieldStorage()

wea = {
    "nombre": form.getvalue('nombre'),
    "serie": form.getvalue('serie'),
    "image_url": form.getvalue('image_url')
}

fsc = "C:/Users/Coke/Desktop/Cyber oso/waifus_data/" + form.getvalue('nombre') + ".json"
if 'file_name' in form:
    fsc = form.getvalue('file_name')

with open(fsc, 'w') as f:
    json.dump(wea, f, indent=4)

print("Content-type:text/html\r\n\r\n")
with open("C:/Users/Coke/Desktop/wea/exitoso.html", 'r') as f:
    print(f.read())