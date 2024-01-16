from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class Question(models.Model):
    Quizmaster = models.CharField(max_length=32)
    Question = models.CharField(max_length=200)
    Answer1 = models.CharField(max_length=150)
    Answer2 = models.CharField(max_length=150)
    Answer3 = models.CharField(max_length=150)
    Answer4 = models.CharField(max_length=150)
    
    CorrectAnswerIndex = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(3)]
        )
    
    
    def __str__(self):
        return f"{self.id} : {self.Question}"


class QuizLibary(models.Model):
    Quizmaster = models.CharField(max_length=32)   
    Questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return  f"{self.id} : {self.Quizmaster}"
    



    