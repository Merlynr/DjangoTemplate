from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginIn', views.user_login),
    path('loginOut', views.user_logout),
    path('userInfo', views.diff_response),

]
