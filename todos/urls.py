from django.conf.urls import url
from todos import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
]
