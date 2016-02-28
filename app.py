__author__ = 'Mary'

from flask import Flask, render_template, request, redirect
from xml.etree.ElementTree import Element, SubElement, tostring

app = Flask(__name__)
file = ""
person = Element("person")
meno = ""
priezvisko = ""

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

def writeToTheFile():
    global file
    file = open("D:/" + meno + "_" + priezvisko + ".xml","w")
    file.write(tostring(person))
    file.close()

def addDataToForm(form, element, subelement):
    print form
    elem = SubElement(person, element)
    for key in form.keys():
        for value in form.getlist(key):
            subelem = SubElement(elem, subelement)
            subelem.text = value

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

@app.route("/position", methods = ['POST'])
def position():
    global meno
    meno = request.form['meno']
    global priezvisko
    priezvisko = request.form['priezvisko']
    izba = request.form['izba']
    clen = request.form['clen']
    pravety = request.form['pravety']
    #TODO uncomment!
    writeBasicData(meno, priezvisko, izba, clen, pravety)
    f = request.form
    print(f)
    return render_template('first.html', name = meno)
    #return "Form has been saved. Thanks. "

@app.route("/skills", methods = ['POST'])
def skills():
    form = request.form
    addDataToForm(form, "positions", "position")
    return render_template('second.html', name = meno)

@app.route('/third', methods = ['POST'])
def some_function():
    form = request.form
    addDataToForm(form, "skills", "skill")
    writeToTheFile()
    return render_template('last.html', meno = meno, priezvisko = priezvisko)

@app.route("/finish", methods = ['POST'])
def justPrint():
    writeToTheFile()
    return render_template("last.html")


if __name__ == '__main__':
    app.run()
