from django.http import HttpResponse


def home(request):
    return HttpResponse("This is our first page music 2")
