from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as rest_views
from weather import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.log_out, name='logout'),
    path('api-docs/', views.api_docs, name='api_docs'),
    path('api/', include('weather.urls')),
    path('api-token-auth/', rest_views.obtain_auth_token),
    path('admin/', admin.site.urls),
]