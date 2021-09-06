from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from authentication.views import UserProfile, search, follow,home
from direct.views import UserSearch


urlpatterns = [
   	path('search/', search, name='search'),
    path('admin/', admin.site.urls),
    path('',home,name ='home'),
    path('post/', include('post.urls')),
    path('direct/', include('direct.urls')),
    path('new/', UserSearch, name='usersearch'),
    path('user/', include('authentication.urls')),
    path('notifications/', include('notifications.urls')),
    path('<username>/', UserProfile, name='profile'),
    path('<username>/saved', UserProfile, name='profilefavorites'),
    path('<username>/follow/<option>', follow, name='follow'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)