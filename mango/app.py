from api import API

app=API()

@app.route("/")
def home(request, response):
    response.text = "welcome to the home page"

@app.route("/about")
def about(request, response):
    response.text = "welcome to the about page"

@app.route('/hello/{name}')
def say_hello(request, response, name):
    response.text = f"hello, {name}"