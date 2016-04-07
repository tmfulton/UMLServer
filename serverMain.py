from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Add /uml to the end of the address to generate UML!"

@app.route("/smell/<name>")
def smelly(name):
    out = name + " smells"
    return out

@app.route("/uml")
def generateUML():
    cmd = ["java", "-jar", "./plantuml.jar", "./plantUMLTest.txt"]
    p = subprocess.Popen(cmd)
    return "Creating your Diagram now"

if __name__ == "__main__" :
    app.run()