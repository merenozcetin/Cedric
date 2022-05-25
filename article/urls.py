from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('',views.thoughts,name="thoughts"),
    path('addthought/',views.addthought,name="addthought"),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('thoughts1/',views.thoughts1,name="thoughts1"),
    path('comment/<int:id>',views.addComment,name="comment"),
]