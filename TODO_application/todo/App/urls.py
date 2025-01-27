from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    
    path('signup/',views.signup),
    path('login/',views.loginUser, name="login"),
    path('todopage/',views.todopage),
    path('edit_todo/<str:srno>',views.edit_todo,name='edit_todo'),
    path('delete_todo/<str:srno>',views.delete_todo),
    path('signout',views.signout,name='signout'),
]