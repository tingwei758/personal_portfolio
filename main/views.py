from django.shortcuts import render
from .models import Code

# Create your views here.

def homepage(request):
    code = Code.objects.get(pk=1)
    context = {
        "code": code,
    }
    return render(request, 'homepage.html', context)