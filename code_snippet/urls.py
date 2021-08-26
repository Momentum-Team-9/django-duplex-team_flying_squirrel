"""code_snippet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from core import views as views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('users', views.user, name='users'),
    path('user/<int:pk>/profile', views.user_profile, name='user_profile'),
    path('user/<int:pk>/profile/edit', views.edit_profile, name='edit_profile'),
    path('feed/', views.feed, name='feed'),
    path('', views.index, name='index'),
    path('snippet/<int:pk>', views.snippet, name='snippet'),
    path('user/<int:pk>/profile/snippet/add', views.add_snippet, name='add_snippet'),
    path('user/<int:pk>/profile/snippet/edit', views.edit_snippet, name='edit_snippet'),
    path('snippet/<int:pk>/delete', views.delete_snippet, name='delete_snippet'),
    path('search/', views.snippet_search, name='snippet_search'),
    path('user/<int:pk>/profile/search', views.profile_search, name='profile_search'),
    path('snippet/<int:snippetPK>/copy', views.copy_snippet, name='copy_snippet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

