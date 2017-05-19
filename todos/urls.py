from django.conf.urls import url
from todos import views, views_api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^save$', views.save, name='save'),
    url(r'^edit/todos/(\d+)$', views.edit, name='edit'),

    # API Route for Ajax
    url(r'^api/todos/(\d+)$', views_api.update, name='api_update_todo')
]
