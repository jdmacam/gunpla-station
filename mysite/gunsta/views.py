from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title": "Gunpla Station"
    }

    return render(request, "index.html", context=context)