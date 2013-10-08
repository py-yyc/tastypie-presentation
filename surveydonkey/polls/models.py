from django.db import models


class Question(models.Model):
    description = models.CharField(max_length=200, help_text="The actual question")
    pub_date = models.DateTimeField('date published', help_text="The date and time the question was published")

    def __unicode__(self):
        return self.description


class Choice(models.Model):
    question = models.ForeignKey(Question, help_text="The question that this is a choice for")
    description = models.CharField(max_length=200, help_text="The text for the choice")
    votes = models.IntegerField(default=0, help_text="The number of votes this choice has")

    def __unicode__(self):
        return self.description