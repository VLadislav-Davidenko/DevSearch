from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        # is_valid Django method to check if the submition was valid
        if form.is_valid():
            # it gives us the instance of current project
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')


    contex = {'form': form}
    return render(request, "projects/project_form.html", contex)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    # instance - to specify what column we will modify
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # is_valid Django method to check if the submition was valid
        if form.is_valid():
            # save Django method to save info and add it to db
            form.save()
            return redirect('projects')


    contex = {'form': form}
    return render(request, "projects/project_form.html", contex)

@login_required(login_url='login')
def deleteProject(request, pk):
    # We take info from authorised user
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    contex = {'object': project}
    return render(request, 'projects/delete_template.html', contex)