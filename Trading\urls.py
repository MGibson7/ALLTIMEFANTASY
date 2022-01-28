from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#URLCONFIGURATION
urlpatterns = [
    path('', views.trades),
    path('add/', views.add),
]

urlpatterns += staticfiles_urlpatterns()
