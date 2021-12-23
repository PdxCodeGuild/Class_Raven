from django.db import models

class Question(models.Model):
    # db columns are represented as 'fields'
    question_text = models.CharField(max_length=200)

    # auto_now_add auto-populates the date with the current
    # date/time when an object is created in the database
    pub_date = models.DateTimeField(auto_now_add=True)

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