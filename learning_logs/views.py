from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """The home page for Topics List."""
    return render(request, 'learning_logs/topics.html')