from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("This is my home page (/)")
    context = {'name': 'Nhat', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is my about page (/)")
    return render(request, 'about.html')
def projects(request):
    # return HttpResponse("This is my project page (/)")
    return render(request, 'projects.html')
def contact(request):
    # return HttpResponse("This is my contact page (/)")
    return render(request, 'contact.html')