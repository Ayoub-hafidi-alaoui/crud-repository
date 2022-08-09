"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from github.views import all_repositories, show_repository, new_repository, edit_repository, delete_repository

urlpatterns = [
    path('admin/', admin.site.urls),
    path("repositories/", all_repositories, name='all_repositories'),
    path("repositories/new", new_repository, name='new_repository'),
    path("repositories/<int:id>", show_repository, name = "show_repository"),
    path("repositories/<int:id>/edit", edit_repository, name = "edit_repository"),
    path("repositories/<int:id>/delete", delete_repository, name = "delete_repository")
]
