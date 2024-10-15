from webob import Request, Response
from parse import parse

class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def handle_request(self, request):
        response = Response()
        try:
            handler, name = self.find_handler(request)
        finally:
            handler = self.find_handler(request)
        if handler is not None:
            if name:
                handler(request, response, name)
            handler(request, response)
        else:
            self.defaultResponse(response)

        return response
    
    def find_handler(self, request):
        for path, handler in self.routes.items():
            if path == request.path:
                try:
                    para1 = path.split("/")[:1]
                    if para1 == "hello":
                        result = parse('/hello/{name}', path)
                        name = result.named['name']
                        return handler, name
                finally: 
                    return handler
    
    def defaultResponse(self, response):
        response.status_code = 404
        response.text = "Page not found"