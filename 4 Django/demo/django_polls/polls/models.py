from django.db import models

# import the CustomUser model from the users app
from users.models import CustomUser

STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed')
]


class Question(models.Model):
    # user the created the Question
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='questions')

    # db columns are represented as 'fields'
    question_text = models.CharField(max_length=200)

    # auto_now_add auto-populates the date with the current
    # date/time when an object is created in the database
    pub_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    # models.CASCADE means that when a question is deleted, 
    # the deletion 'cascades' onto its choices (thus deleting them)
    # related_name is the attribute name by which a questions choices are retrieved
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text} - votes: {self.votes}"