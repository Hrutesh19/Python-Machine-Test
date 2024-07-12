from django.db import models

# Create your models here.
class client(models.Model):
    client_name=models.CharField(max_length=100)
    client_email=models.EmailField(max_length=200)

class project(models.Model):
    project_name=models.CharField(max_length=50)
    project_desc=models.CharField(max_length=50)
    client=models.ForeignKey(client, on_delete=models.CASCADE)
    
class user(models.Model):
    user_name=models.CharField(max_length=100)
    project=models.ForeignKey(project,on_delete=models.CASCADE)

