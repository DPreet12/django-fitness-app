from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import LoginRequiredMixin

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Hello</h1>')

class Home(LoginView):
    template_name= 'home.html'

def about(request):
    return render(request, 'about.html')

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

def profile_detail(request):
    try:
        profile = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        return redirect('home')
    return render(request, 'profiles/details.html', {'profile': profile})

class ProfileUpdate(UpdateView):
    model = Profile
    fields = [ 'age', 'weight', 'height']
    template_name = 'main_app/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self, querySet=None):
        return Profile.objects.get(user= self.request.user)

class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'main_app/profile_confirm_delete.html'
    success_url = reverse_lazy('signup')

    def get_object(self, querySet = None):
        return Profile.objects.get(user= self.request.user)