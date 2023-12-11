from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    context = {
        "title": "eLearning",
    }

    return render(request, "home.html", context)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change 'home' to your desired homepage URL
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})