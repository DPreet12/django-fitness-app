from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile_detail, name='profile'),
    path('profile/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('profile/delete/', views.ProfileDelete.as_view(), name='profile-delete'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile-create'),
]
