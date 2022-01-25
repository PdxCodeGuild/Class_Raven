from django.db import models
from django.db.models import Model

class key_list(models.Model):
    key_id = models.CharField(max_length = 100)
    key_for = models.CharField(max_length = 100)   
    available_status = models.BooleanField()

class key_user(models.Model):
    user_id = models.CharField(max_length= 100)
    user_name = models.CharField(max_length= 100)  

class key_issue(models.Model):
    key_id = models.ForeignKey(key_list, on_delete = models.CASCADE)
    user_id = models.ForeignKey(key_user, on_delete = models.CASCADE)
    issue_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    user_sign_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    return_due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    

    
