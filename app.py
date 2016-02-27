__author__ = 'Mary'

from flask import Flask, render_template, request, redirect
from xml.etree.ElementTree import Element, SubElement, tostring

app = Flask(__name__)
file = ""
person = Element("person")

def writeBasicData(meno, priezvisko, izba, clen, pravety):

    firstName = SubElement(person, "firstName")
    firstName.text = meno
    lastName = SubElement(person, "lastName")
    lastName.text = priezvisko
    room = SubElement(person, "room")
    room.text = izba
    member =SubElement(person, "member")
    member.text = clen
    text = SubElement(person, "text")
    text.text = pravety
    global file
    file = open("D:/" + meno + "_" + priezvisko + ".xml","w")
    file.write(tostring(person))
    file.close()
#    writeMoreData(clen, pravety)

# def writeMoreData(clen, pravety):
#     cclen = SubElement(person, "clen")
#     cclen.text = clen
#     print clen
#     global file
#     with open(file.name, "a") as f:
#         f.write(tostring(person))
#         f.close()

@app.route("/")
def hello():
    return render_template('index.html', author="me", name="you")

@app.route("/first", methods = ['POST'])
def signup():
    meno = request.form['meno']
    priezvisko = request.form['priezvisko']
    izba = request.form['izba']
    clen = request.form['clen']
    pravety = request.form['pravety']
    writeBasicData(meno, priezvisko, izba, clen, pravety)


    return "Form has been saved. Thanks. "

@app.route("/data")
def writeData():
    return "nothing"


if __name__ == '__main__':
    app.run()
