from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        db_table = 'tasks'