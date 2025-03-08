"""
URL configuration for skill_sharing_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile_redirect, name='profile_redirect'),
    path('profile/<str:username>/', profile, name='profile'),
    path('feedback/<str:username>/', feedback, name='feedback'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('search/', search, name='search'),
    path('send-request/<str:username>/', send_request, name='send_request'),
    path('view-requests/', view_requests, name='view_requests'),
    path('accept-request/<int:request_id>/', accept_request, name='accept_request'),
    path('decline-request/<int:request_id>/', decline_request, name='decline_request'),
    path('submit-feedback/<int:request_id>/', submit_feedback, name='submit_feedback'),
    path('confirm-logout/', confirm_logout, name='confirm_logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
