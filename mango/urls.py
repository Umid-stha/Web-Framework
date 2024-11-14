from .api import path
from . import views

urlpatterns = [
    path("/", views.home),
    path("/hello/{name}", views.say_hello)
]