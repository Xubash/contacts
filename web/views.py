from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello user, Xubash welcomes you to the Contact Web Application.")