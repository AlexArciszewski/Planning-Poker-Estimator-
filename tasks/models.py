from django.db import models

from sprints.models import Sprint
from django.contrib.auth.models import User



class Task(models.Model):
    title = models.CharField(max_length=150, help_text='Title of the task')

    description = models.TextField(help_text='Description of the task')

    created_at = models.DateField(auto_now_add=True, help_text='Date of creation of the task')

    product_owner = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True, help_text='Product owner of the task', related_name='owned_tasks')

    user_story = models.CharField(max_length=5, help_text='User story number', null=True, blank=True)

    created_by = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True, help_text='User who created the task', related_name='created_tasks')

    sprint = models.ForeignKey(Sprint, max_length=150, on_delete=models.CASCADE, null=True, related_name='tasks')

















    # tu chyba zrobię ForeignKey(z klasy Task z pliku z modelami z tasks)
#     importuję klasę.Sprint z pliku models w folderze sprints.... przed Sprint powinnna być nazwa pliku models ale czy
#     to nie spowoduje szukania w modelsach gdzie jest user? taka konstrukcja chyba robi blad



# Create your models here.

