import cgi, cgitb
import json
import os

form = cgi.FieldStorage()

print("Content-type:text/html\r\n\r\n")

with open("C:/Users/Coke/Desktop/wea/header.html") as f:
    print(f.read())

print("<div class=\"container p-3 my-3 bg-dark text-white align-self-center rounded\">")
print("<div class=\"bs-example\">")
print("<form action=\"/cgi-bin/updater.py\" method=\"post\">")
print("<div class=\"form-group\">")
print("<label for=\"coso\">Waifu a updatear</label>")
print("<select name=\"waifu\" class=\"form-control\" id=\"coso\">")

for x in os.listdir("C:/Users/Coke/Desktop/Cyber oso/waifus_data/"):
    print("<option value=\"" + x + "\">" + x + "</option>")

print("</select>")
print("</div>")
print("<input class=\"btn btn-primary\" type=\"submit\" value=\"Seleccionar\" />")
print("</form>")
print("</div>")
print("</div>")

with open("C:/Users/Coke/Desktop/wea/footer.html") as f:
    print(f.read())