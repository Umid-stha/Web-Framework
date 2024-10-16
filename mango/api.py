from webob import Request, Response
from parse import parse
import inspect

class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def route(self, path):
        def wrapper(handler):
            for existing_path, existing_handler in self.routes.items():
                if path == existing_path:
                    raise AssertionError("Same path can't be repeated for diffrent functions")
            self.routes[path] = handler
            return handler
        return wrapper

    def handle_request(self, request):
        response = Response()
        handler, kwargs = self.find_handler(request)
        print(handler, kwargs)
        if handler is not None:
            if inspect.isClass(handler):
                handler_func = getattr(handler(), request.method.lower(), None)
            else:
                handler(request, response, **kwargs)
        else:
            self.defaultResponse(response)
        return response
    
    # own solution
    # def find_handler(self, request):
    #     for path, handler in self.routes.items():
    #         para1 = path.split("/")[1:2]
    #         print(para1)
    #         if para1 == "hello":
    #             result = parse('/hello/{name}', path)
    #             name = result.named['name']
    #             return handler, name
    #         else:
    #             if path == request.path:
    #                 print(path)
    #                 return handler, None
    #         return None, None

    #tutorial
    def find_handler(self, request):
        for path, handler in self.routes.items():
            result = parse(path, request.path)
            if result is not None:
                name = result.named
                return handler, name
        return None, None 
        
    def defaultResponse(self, response):
        response.status_code = 404
        response.text = "Page not found"