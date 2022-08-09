from django.db import models

# Create your models here.


class Github(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    repositoryName = models.CharField(max_length=100)
    repositoryDescription = models.TextField(max_length=1000)
    commits = models.TextField(max_length=1000)
    stars = models.IntegerField(null=True)
    tags = models.CharField(max_length=100)
    issues = models.CharField(max_length=100)
    followers = models.IntegerField(null=True)
    following = models.IntegerField(null=True)
    pullRequestsName = models.CharField(max_length=100)
    pullRequestsStatus = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.repositoryName
    
    