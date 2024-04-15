from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Assuming you have a 'home.html' template
