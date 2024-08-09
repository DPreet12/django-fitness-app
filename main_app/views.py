from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Workout, Goal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Hello</h1>')

class Home(LoginView):
    template_name= 'home.html'



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile.objects.create(user=user)
            login( request, user )
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def profile_detail(request):
    try:
        profile = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        return redirect('profile-create')
        # return render(request, 'profiles')
    return render(request, 'profiles/details.html', {'profile': profile})


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['age', 'weight', 'height', 'gender']
    template_name = 'main_app/profile_form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = [ 'age', 'weight', 'height', 'gender']
    template_name = 'main_app/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self, querySet=None):
        return Profile.objects.get( user= self.request.user)

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'main_app/profile_confirm_delete.html'
    success_url = reverse_lazy('profile-create')

    def get_object(self, querySet = None):
        return Profile.objects.get( user= self.request.user)

 
@login_required
def workout_details(request):
    workouts = Workout.objects.filter(user = request.user).order_by('date')
    return render(request, 'workouts/workout_details.html', {'workouts': workouts})
  
class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['date', 'exercise', 'duration', 'distance', 'notes']
    template_name = 'main_app/workout_form.html'
    success_url = reverse_lazy('workout-details')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['date', 'exercise', 'duration', 'distance', 'notes']
    template_name = 'main_app/workout_form.html'
    success_url = reverse_lazy('workout-details')

    def get_object(self, querySet=None):
        workout_id = self.kwargs["pk"]
        workout = Workout.objects.get(id=workout_id,  user= self.request.user)
        return workout

class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'main_app/workout_confirm_delete.html'
    success_url = reverse_lazy('workout-details')

    def get_object(self, querySet = None):
        workout_id = self.kwargs.get('pk')
        return Workout.objects.get(id= workout_id, user = self.request.user)
    
@login_required
def goal_details(request):
    goals = Goal.objects.filter(user = request.user)
    return render(request, 'main_app/goals/goal_details.html', {'goals': goals})

class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    template_name = 'main_app/goal_form.html'
    fields = ['target_weight', 'target_date', 'target_purpose']
    success_url = reverse_lazy('goal-details')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GoalUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = ['target_weight', 'target_date', 'target_purpose']
    template_name = 'main_app/goal_form.html'
    success_url = reverse_lazy('goal-details')

    def get_object(self, querySet=None):
        goal_id = self.kwargs.get('pk')
        return Goal.objects.get(id = goal_id, user = self.request.user)
    
class GoalDelete(LoginRequiredMixin, DeleteView):
    model = Goal
    template_name = 'main_app/goal_confirm_delete.html'
    success_url = reverse_lazy('goal-details')

    def get_object(self, querySet= None):
        goal_id = self.kwargs.get('pk')
        return Goal.objects.get(id= goal_id, user = self.request.user)


 