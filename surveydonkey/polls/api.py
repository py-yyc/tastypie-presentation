from tastypie.resources import ModelResource
from polls.models import Question, Choice


class ChoiceResource(ModelResource):
    class Meta:
        queryset = Choice.objects.all()


class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()