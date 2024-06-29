from . import views

from django.urls import path

urlpatterns = [
    path('',views.notes_index,name='notes_index'),
    path('dashboard/',views.notes_list,name='notes_list'),
    path('create/',views.notes_create,name='notes_create'),
    path('<int:tweet_id>/edit/',views.notes_edit,name='notes_edit'),
    path('<int:tweet_id>/delete/',views.notes_delete,name='notes_delete'),
    path('register/',views.register,name="register"),
]
