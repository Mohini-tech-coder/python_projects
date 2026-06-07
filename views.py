from django.shortcuts import render, redirect
from .forms import FoodEntryForm
from .models import FoodEntry
def home(request):

    if request.method == 'POST':
        form = FoodEntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = FoodEntryForm()

    foods = FoodEntry.objects.all()

    return render(request, 'home.html', {
        'form': form,
        'foods': foods
    })


def dashboard(request):
    return render(request, 'dashboard.html')


def diet(request):
    return render(request, 'diet.html')


def exercise(request):
    return render(request, 'exercise.html')


def water(request):
    return render(request, 'water.html')


def bmi(request):
    return render(request, 'bmi.html')


def recommendation(request):
    return render(request, 'recommendation.html')


def about(request):
    return render(request, 'about.html')


def login_page(request):
    return render(request, 'login.html')


def signup_page(request):
    return render(request, 'signup.html')