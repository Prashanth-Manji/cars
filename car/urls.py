from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('Add',views.Add,name='Add'),
    path('see',views.see,name='see'),

]
