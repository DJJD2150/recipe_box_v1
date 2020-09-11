"""recipe_box_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from recipe_box_app import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('edit/<int:recipe_id>/', views.edit_recipe_view),
    path('favorite/<int:recipe_id>/', views.add_favorite_view),
    path('unfavorite/<int:recipe_id>/', views.remove_favorite_view),
    path('author/<int:author_id>/', views.author_view),
    path('recipe/<int:recipe_id>/', views.recipe_view),
    path('myfavorites/', views.my_favorites_view),
    path('addauthor/', views.add_author, name="addauthor"),
    path('addrecipe/', views.add_recipe, name="addrecipe"),
    path('login/', views.login_view, name="loginview"),
    path('logout/', views.logout_view, name="logoutview"),
    path('signup/', views.signup_view, name="signupview"),
    path('forbidden/', views.forbidden),
    path('admin/', admin.site.urls),
]
