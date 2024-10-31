from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('categories/', views.catgories, name="categories"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change-password/', views.logout_page, name='password-change'),
    path('delete-anime/<int:id>/', views.delete_anime, name="delete-anime"),
    path('anime_view/<int:id>/', views.anime_view, name='anime_view')
   

]