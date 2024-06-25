from django.db import models
from datetime import date


class Task(models.Model):
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name="ID"),
    title = models.CharField(max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        db_table = 'tasks'
        ordering = ['deadline']

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()