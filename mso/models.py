from django.db import models

# MSO table
class Mso(models.Model):
    requested_by = models.CharField(max_length=100, default='')
    section =  models.CharField(max_length=100, default='')
    department_head =  models.CharField(max_length=100, default='')
    location =  models.CharField(max_length=100, default='')
    description_of_service = models.TextField(default='')
    manager_approval = models.BooleanField(default=False)
    manager_approval_date = models.DateTimeField(auto_now=False, null=True)
    actual_work_descripition = models.TextField(default='')
    date_started = models.CharField(default='', max_length=50)
    date_completed = models.CharField(default='', max_length=50)
    work_compleated_by = models.TextField(default='')
    id_number = models.CharField(max_length=254, default='')
    supervisor_approval = models.BooleanField(default=False)
    supervisor_approval_date = models.DateTimeField(auto_now=False, null=True)
    posted_on = models.DateTimeField(auto_now=True)
    posted_by = models.EmailField(max_length=254, default='')
    posted_by_name = models.CharField(max_length=254, default='')
    requested_by_other_department = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)