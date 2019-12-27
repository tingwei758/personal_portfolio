from django.shortcuts import render, redirect
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, url):
    project = Project.objects.get(url=url)
    return redirect(project.filename)