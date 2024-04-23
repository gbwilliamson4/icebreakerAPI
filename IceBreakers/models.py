from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200)
    contributor = models.CharField(max_length=30, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.question
