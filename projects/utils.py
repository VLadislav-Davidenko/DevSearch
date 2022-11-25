from .models import Project, Tag
from django.db.models import Q

def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    # Adding distinct() allows us to get only one instance of each user
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | 
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tags) |
        Q(description__icontains=search_query)
        )

    return projects, search_query