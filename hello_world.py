from flask import Flask

app = Flask(__name__)

# static
@app.route("/hello")
def hello_world():
    return "Hello World!"

# dynamic

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last): 
    jediName = last[:3] + first[:2]
    return "Hello, Jedi {}".format(jediName)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)