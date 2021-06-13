



from django.urls import path
from .views import home,index,create_todo,list_all_todo,delete_todo,update_todo,registration,signin
urlpatterns=[
    path('',home,name="homepage"),
    path('index',index,name="index"),
    path('create/',create_todo,name="create"),
    path('list/',list_all_todo,name="list"),
    path('delete/<int:id>',delete_todo,name="delete_todo"),
    path('update/<int:id>',update_todo,name="update_todo"),
    path('account',registration,name="registration"),
    path('login',signin,name="login")
    ]