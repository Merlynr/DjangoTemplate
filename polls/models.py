# Create your models here.


from django.db import models


class Question(models.Model):
    nums = models.IntegerField(default=0)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Records(models.Model):
    records = models.CharField(max_length=200)
