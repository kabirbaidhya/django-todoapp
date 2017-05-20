from django.conf.urls import url
from todos import views, views_api, auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^save$', views.save, name='save'),
    url(r'^edit/todos/(\d+)$', views.edit, name='edit'),

    # API Route for Ajax
    url(r'^api/todos/(\d+)$', views_api.update, name='api_update_todo'),

    # Auth Routes
    url(r'^login$', auth_views.login, name='login'),
    url(r'^authenticate$', auth_views.authenticate, name='authenticate'),
]
