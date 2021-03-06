from django.urls import path     
from . import views
urlpatterns = [
   path('', views.index),
   path('new', views.newz),
   path('create', views.create),
   path('<int:num>', views.show),
   path('<int:num>/edit', views.edit),
   path('<int:num>/delete', views.destroy)
]