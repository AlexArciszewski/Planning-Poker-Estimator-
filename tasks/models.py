from django.db import models
from sprints.models import Sprint
from django.contrib.auth.models import User


class Task(models.Model):
    """model of Task"""

    title = models.CharField(max_length=150, help_text='Title of the task')
    description = models.TextField(help_text='Description of the task')
    created_at = models.DateField(auto_now_add=True, help_text='Date of creation of the task')
    product_owner = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True,
                                      help_text='Product owner of the task', related_name='owned_tasks')
    user_story = models.CharField(max_length=5, help_text='User story number', null=True, blank=True)
    created_by = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True,
                                   help_text='User who created the task', related_name='created_tasks')
    sprint = models.ForeignKey(Sprint, max_length=150, on_delete=models.CASCADE, null=True, related_name='tasks')

# user = User.objects.get(id=1)
# user.created_tasks.all() # wyciągnie mi wszystkie taski, które są przyspiane do User'a.
# Task.objects.filter(created_by=user)
class TaskEstimation(models.Model):
    """model of task estimation"""

    ESTIMATION_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "5"),
        ("5", "8"),
        ("6", "13"),
        ("7", "21"),
    )

    estimation = models.CharField(choices=ESTIMATION_CHOICES,max_length=150)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, help_text='Who estimated the task',
                             related_name='estimations')
    created_at = models.DateField(auto_now_add=True, help_text='Date of task estimation')
    estimated_by = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True,
                                     help_text='User who estimated the task', related_name='estimations')
    # user.estimations.all()
    class Meta:
        """Connecting task with the estimators"""
        unique_together = ('task', 'estimated_by')


class TeamMember(models.Model):
    """team member task alocation"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
#
#



