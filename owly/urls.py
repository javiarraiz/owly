
from django.contrib import admin
from django.urls import path, include
from owly_app.views import main, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('', main, name='main'),
    #path('dashboard/', dashboard, name='dashboard'),
    path('api/', include('users.api.urls')),
]
