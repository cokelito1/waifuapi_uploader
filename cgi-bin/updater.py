import cgi, cgitb
import json
import requests
import os

form = cgi.FieldStorage()
coso = form.getvalue('waifu')

req = requests.get("http://localhost:3000/api/waifus/" + coso)

print("Content-type:text/html\r\n\r\n")
with open("C:/Users/Coke/Desktop/wea/header.html") as f:
    print(f.read())

wn = req.json()

print("<div class=\"container p-3 my-3 bg-dark text-white align-self-center rounded\">")
print("<div class=\"bs-example\">")
print("<form action=\"/cgi-bin/update.py\" method=\"post\">")

print("<div class=\"form-group\">")
print("<label for=\"name\">Nombre de la minita</label>")
print("<input type=\"text\" id=\"name\" name = \"nombre\" value=\"" + wn["nombre"] + "\">")
print("</div>")

print("<div class=\"form-group\">")

series = {}
nombre="whatwea"
r_series = requests.get("http://localhost:3000/api/series")
for serie in r_series.json():
    series[serie["nombre"]] = serie["_id"]
    if serie["_id"] == wn["serie_id"]:
        nombre = serie["nombre"]

print("<label for=\"serie\">Serie de la minita</label>")
print("<select name=\"serie\" class=\"form-control\" id=\"serie\">")
print("<option value=\"" + wn["serie_id"] + "\">" + nombre + "</option>")
for key in series:
    if series[key] != wn["serie_id"]:
        print("<option value=\"" + series[key] + "\">" + key + "</option>")

print("</select>")
print("</div>")

print("<div class=\"form-group\">")
print("<label for=\"url\">URL del gif de la minita</label>")
print("<input id=\"url\" type=\"text\" name=\"image_url\" value=\"" + wn["image_url"] + "\">")
print("</div>")

print("<div class=\"form-group\">")
print("<input type=\"text\" name=\"file_name\" value=\"" + coso + "\" readonly>")
print("</div>")
    
print("<input class=\"btn btn-primary\" type=\"submit\" value=\"Updatear\" />")
print("</form>")
print("</div>")
print("</div>")


with open("C:/Users/Coke/Desktop/wea/footer.html") as f:
    print(f.read())