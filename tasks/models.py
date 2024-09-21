from django.db import models
from sprints.models import Sprint
from django.contrib.auth.models import User


class Task(models.Model):
    """Model of Task"""

    title = models.CharField(max_length=150, help_text='Title of the task')
    description = models.TextField(help_text='Description of the task')
    created_at = models.DateField(auto_now_add=True, help_text='Date of creation of the task')
    product_owner = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True,
                                      help_text='Product owner of the task', related_name='owned_tasks')
    user_story = models.CharField(max_length=5, help_text='User story number', null=True, blank=True)
    created_by = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True,
                                   help_text='User who created the task', related_name='created_tasks')
    sprint = models.ForeignKey(Sprint, max_length=150, on_delete=models.CASCADE, null=True, related_name='tasks')


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

    estimation = models.CharField(choices=ESTIMATION_CHOICES, max_length=150)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, help_text='Who estimated the task',
                             related_name='estimations', null=False)
    created_at = models.DateField(auto_now_add=True, help_text='Date of task estimation')
    estimated_by = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE, null=True,
                                     help_text='User who estimated the task', related_name='estimations')

    class Meta:
        """Connecting task with the estimators"""
        unique_together = ('task', 'estimated_by')

    def __str__(self):
        # return estimation value from the ESIMATED_CHOICES dict by they key from number position of the scroll bar"
        choices_dict = dict(self.ESTIMATION_CHOICES)
        if self.estimation in choices_dict:
            return choices_dict[self.estimation]
        else:
            return self.estimation


class TeamMember(models.Model):
    """team member task alocation"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)




