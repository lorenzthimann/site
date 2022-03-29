from django.db import models
from account.models import User

class Exercice(models.Model):
    name = models.CharField(max_length=50)

class TimedExercice(models.Model):
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE, related_name="timed_exercice_exercice")

    minutes = models.IntegerField()
    seconds = models.IntegerField()

class TrainingPlan(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    timed_exercices = models.ManyToManyField(TimedExercice)

