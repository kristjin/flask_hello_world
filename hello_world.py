from flask import Flask, render_template

app = Flask(__name__)

# static
@app.route("/hello")
def hello_world():
    return render_template('hello_world.html')

# dynamic

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello_template.html',
                           name=name
                          )

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    return render_template('jedi_template.html',
                           first=first,
                           last=last)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)