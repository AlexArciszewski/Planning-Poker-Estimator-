from django.db import models
from django.contrib.auth.models import User


class Sprint(models.Model):

    sprint_id = models.CharField(max_length=150)

    sprint_title = models.CharField(max_length=150)

    sprint_info = models.CharField(max_length=450)

    date_posted = models.DateField(auto_now_add=True)

    po_name = models.CharField(max_length=150)


    user = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True)
