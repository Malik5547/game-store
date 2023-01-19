from django.http import HttpResponse


# Create your views here.
def index(requse):
    return HttpResponse("Welcome to the best video game store.")