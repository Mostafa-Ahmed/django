from django.http import HttpResponse


def index(request):
    return HttpResponse('<H1>this tha Music app homepage <H1>')
