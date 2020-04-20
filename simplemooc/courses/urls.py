from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>', views.details, name='details'),
    # re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    # re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
]
