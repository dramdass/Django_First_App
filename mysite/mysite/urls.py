from django.conf.urls import patterns, include, url
from tastypie.api import Api
from polls.api import PollResource, ChoiceResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    #tastypie api
    url(r'^api/', include(v1_api.urls)),
)
