from django.shortcuts import render, HttpResponse
from home.models import Contact
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
    if request.method=="POST":
        email = request.POST['email']
        question = request.POST['question']
        # print(email, question)
        contact = Contact(email=email, question=question)
        contact.save()
        print("the data has been written to the DB")
    # return HttpResponse("This is my contact page (/)")
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog1.html')