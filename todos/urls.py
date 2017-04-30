from django.conf.urls import url
from todos import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^save$', views.save, name='save')
]
