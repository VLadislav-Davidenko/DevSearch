from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {'project': projectObj})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        # is_valid Django method to check if the submition was valid
        if form.is_valid():
            # save Django method to save info and add it to db
            form.save()
            return redirect('projects')


    contex = {'form': form}
    return render(request, "projects/project_form.html", contex)


def updateProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        # is_valid Django method to check if the submition was valid
        if form.is_valid():
            # save Django method to save info and add it to db
            form.save()
            return redirect('projects')


    contex = {'form': form}
    return render(request, "projects/project_form.html", contex)
