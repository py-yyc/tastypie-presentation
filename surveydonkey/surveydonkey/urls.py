from django.conf.urls import patterns, include, url
from polls.api import QuestionResource, ChoiceResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Register the resources with the API registry
v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())
v1_api.register(ChoiceResource())

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Hook up the API registry urls
    url(r'^api/', include(v1_api.urls)),
)
