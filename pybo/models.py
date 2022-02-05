from django.db import models

# Create your models here.
class Question(models.Model):
    subject=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now=True)