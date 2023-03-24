from django.shortcuts import render
def Home(request):
    return render(request,'index.html')
def About(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
