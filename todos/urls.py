from django.conf.urls import url
from todos import views, views_api, auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^save$', views.save, name='save'),
    url(r'^edit/todos/(\d+)$', views.edit, name='edit'),
    url(r'^delete/todos/(\d+)$', views.delete, name='delete'),

    # API Route for Ajax
    url(r'^api/todos/(?P<pk>[0-9]+)$', views_api.TodoItemView.as_view(), name='api_todo_item'),
    url(r'^api/todos$', views_api.TodoListView.as_view(), name='api_todo_list'),

    # Auth Routes
    url(r'^login$', auth_views.login, name='login'),
    url(r'^authenticate$', auth_views.authenticate, name='authenticate'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^signup$', auth_views.signup, name='signup'),
    url(r'^signup/submit$', auth_views.signup_submit, name='signup-submit'),
]
