# polls/api.py
from tastypie import fields
from tastypie.resources import ModelResource
from polls.models import Poll, Choice

class PollResource(ModelResource):
  class Meta:
    queryset = Poll.objects.all()
    # not necessary since it will default to Poll.tolowercase
    resource_name = 'poll'

class ChoiceResource(ModelResource):
  poll = fields.ForeignKey(PollResource, 'poll')
  
  class Meta:
    queryset = Choice.objects.all()
    resource_name = 'choice'
  
