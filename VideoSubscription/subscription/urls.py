from django.urls import path
from . import views


app_name = 'subscription'

urlpatterns = [
    path('registraion', views.UserregisterView.as_view(), name='registraion'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('home', views.HomePageView.as_view(), name='home'),
    path('watch_video/<int:pk>', views.WatchVideoView.as_view(), name='watch_video'),
    path('payment', views.PaymentView.as_view(), name='payment'),
]