from django.db import models

from sprints.models import Sprint

from django.contrib.auth.models import User

class Task(models.Model):

    task_id = models.CharField(max_length=150)

    task_title = models.CharField(max_length=150)

    task_info = models.CharField(max_length=450)

    date_posted = models.DateField(auto_now_add=True)

    po_name = models.CharField(max_length=150)

    task_owner = models.CharField(max_length=150)

    user_story = models.CharField(max_length=5)     #czy jest user story stworzone

    user = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True)

    sprint_connected = models.ForeignKey(Sprint, max_length=150, on_delete=models.CASCADE, null=True, related_name='tasks')
    # tu chyba zrobię ForeignKey(z klasy Task z pliku z modelami z tasks)
#     importuję klasę.Sprint z pliku models w folderze sprints.... przed Sprint powinnna być nazwa pliku models ale czy
#     to nie spowoduje szukania w modelsach gdzie jest user? taka konstrukcja chyba robi blad



# Create your models here.
