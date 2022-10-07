from email.policy import default
from pydoc import describe
import uuid
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    # null - we allowed to create a row in db and do not need to set it
    # blank - we allowed to submit this part empty to db
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # default - type of encryption
    # unique - store only uique id
    # promary_key - use it as id
    # editable - cannot be edited
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_TYPE =(
       ( "up", "Up Vote"),
        ("down", "Down Vote")
    )
   # owner = 
   # CASCADE will delete all the rewies if the project will be deleted
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name