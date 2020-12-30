from django.urls import path
from .views import Shownotifications,DeleteNotification


urlpatterns = [
   	path('', Shownotifications, name='show-notifications'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification'),

]