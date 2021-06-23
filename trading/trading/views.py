from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Nerds! You're at the stocks page!")