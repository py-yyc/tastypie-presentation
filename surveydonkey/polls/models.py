from django.db import models


class Question(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.description


class Choice(models.Model):
    question = models.ForeignKey(Question)
    description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.description