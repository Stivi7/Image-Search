from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/(?P<data>\w+)/$', views.search, name='search'),
    url(r'^latest/$', views.recent, name='recent'),
]