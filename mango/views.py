from api import API

app=API()

def home(request, response):
    response.text = "welcome to the home page"

# @app.route("/")
# def home2(request, response):
#     response.text = "welcome to the home page 2"

# @app.route("/about")
def about(request, response):
    response.text = "welcome to the about page"

# @app.route("/hello/{name}")
def say_hello(request, response, name):
    response.text = f"hello, {name}"

# @app.route("/student/{id:d}")
def student(request, response, id):
    response.text = f"This students Roll no. is {id}"

# @app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"