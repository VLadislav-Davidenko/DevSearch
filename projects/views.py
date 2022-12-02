from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from .utils import searchProjects, paginateProjects


def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects':projects, 'search_query':search_query, 'custome_range': custom_range}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = projectObj
            review.owner = request.user.profile
            review.save()

            projectObj.getVoteCount

            messages.success(request, "Your review was submited")

            return redirect('single-project', pk=projectObj.id)

    return render(request, "projects/single-project.html", {'project': projectObj, 'form': form})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        # is_valid Django method to check if the submition was valid
        if form.is_valid():
            # it gives us the instance of current project
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, "Project was added successfully")
            return redirect('account')


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
            messages.success(request, "Project was updated successfully")
            return redirect('account')


    contex = {'form': form}
    return render(request, "projects/project_form.html", contex)

@login_required(login_url='login')
def deleteProject(request, pk):
    # We take info from authorised user
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project was deleted successfully")
        return redirect('account')
    contex = {'object': project}
    return render(request, 'delete_template.html', contex)