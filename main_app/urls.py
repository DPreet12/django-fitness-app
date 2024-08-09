from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', LoginView.as_view(template_name='home.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name="logout"),
    path('profile/', views.profile_detail, name='profile'),
    path('profile/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('profile/delete/', views.ProfileDelete.as_view(), name='profile-delete'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile-create'),
    path('workout/create/', views.WorkoutCreate.as_view(), name='workout-create' ),
    path('workout/details/', views.workout_details, name='workout-details'),
    path('workout/update/<int:pk>/', views.WorkoutUpdate.as_view(), name='workout-update'), 
    path('workout/delete/<int:pk>', views.WorkoutDelete.as_view(), name='workout-delete'),
    path('goal/details/', views.goal_details, name='goal-details'),
    path('goal/create/', views.GoalCreate.as_view(), name='goal-create'),
    
]
