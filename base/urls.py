from django.urls import path
from .views import Tasklist, Taskcreate, Taskupdate, Taskdelete, Customlogin, Registerpage
from django.contrib.auth.views import LogoutView

urlpatterns = [
               path('login/', Customlogin.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('register/', Registerpage.as_view(), name='register'),
               path('', Tasklist.as_view(), name='tasks'),
               path('create/', Taskcreate.as_view(), name='create'),
               path('update/<pk>/', Taskupdate.as_view(), name='update'),
               path('delete/<pk>/', Taskdelete.as_view(), name='delete'),

    ]