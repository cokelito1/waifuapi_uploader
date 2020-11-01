import cgi, cgitb
import json
import os

form = cgi.FieldStorage()
coso = form.getvalue('waifu')

print("Content-type:text/html\r\n\r\n")
with open("C:/Users/Coke/Desktop/wea/header.html") as f:
    print(f.read())

with open("C:/Users/Coke/Desktop/Cyber oso/waifus_data/" + coso, 'r') as f:
    wn = json.load(f)

    print("<div class=\"container p-3 my-3 bg-dark text-white align-self-center rounded\">")
    print("<div class=\"bs-example\">")
    print("<form action=\"/cgi-bin/create_wea.py\" method=\"post\">")

    print("<div class=\"form-group\">")
    print("<label for=\"name\">Nombre de la minita</label>")
    print("<input type=\"text\" id=\"name\" name = \"nombre\" value=\"" + wn["nombre"] + "\">")
    print("</div>")

    print("<div class=\"form-group\">")
    print("<label for=\"serie\">Nombre de la serie</label>")
    print("<input id=\"serie\" type=\"text\" name=\"serie\" value=\"" + wn["serie"] + "\">")
    print("</div>")

    print("<div class=\"form-group\">")
    print("<label for=\"url\">URL del gif de la minita</label>")
    print("<input id=\"url\" type=\"text\" name=\"image_url\" value=\"" + wn["image_url"] + "\">")
    print("</div>")

    print("<div class=\"form-group\">")
    print("<input type=\"text\" name=\"file_name\" value=\"C:/Users/Coke/Desktop/Cyber oso/waifus_data/" + coso + "\" readonly>")
    print("</div>")
    
    print("<input class=\"btn btn-primary\" type=\"submit\" value=\"Updatear\" />")
    print("</form>")
    print("</div>")
    print("</div>")


with open("C:/Users/Coke/Desktop/wea/footer.html") as f:
    print(f.read())