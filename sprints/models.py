from django.db import models
from django.contrib.auth.models import User


class Sprint(models.Model):
    title = models.CharField(max_length=150, help_text='Title of the sprint')

    description = models.TextField(help_text='Description of the sprint')


    created_at = models.DateField(auto_now_add=True, help_text='Date of creation of the sprint')

    product_owner = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True, help_text='Product owner of the sprint', related_name='owned_sprints')

    # user = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True)

    created_by = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True,help_text='User who created the sprint', related_name='created_sprints')
