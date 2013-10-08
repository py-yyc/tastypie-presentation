from tastypie.resources import ModelResource
from authorizers import CrazyAuthorization
from polls.models import Question, Choice
from serializers import CamelCaseJsonSerializer


class ChoiceResource(ModelResource):
    class Meta:
        queryset = Choice.objects.all()
        allowed_methods = ['get', 'post']
        authorization = CrazyAuthorization()
        serializer = CamelCaseJsonSerializer()


class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        allowed_methods = ['get', 'post']
        authorization = CrazyAuthorization()
        serializer = CamelCaseJsonSerializer()
