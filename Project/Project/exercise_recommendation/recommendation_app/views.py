from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserInfoForm
from .genetic_algorithm import genetic_algorithm  # Import the genetic algorithm function
from .diet_genetic_algorithm import diet_genetic_algorithm
from .forms import RecommendationForm
import subprocess
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def SignInUp(request):
    return render(request, 'recommendation_app/SignInUp.html')

def homePage(request):
    return render(request, 'recommendation_app/index.html')

def dashboard(request):
    return render(request, 'recommendation_app/Dashboard.html')

def help(request):
    return render(request, 'recommendation_app/Help.html')

def goals(request):
    return render(request, 'recommendation_app/Goals.html')

def bmi_calculator(request):
    return render(request, 'recommendation_app/BMI.html')

def diet_recommendation_form(request):
    recommended_foods = None

    if request.method == 'POST':
        form = UserInfoForm(request.POST)

        if form.is_valid():
            user_info = form.cleaned_data
            # Run genetic algorithm to recommend foods
            recommended_foods = diet_genetic_algorithm(user_info)
    else:
        form = UserInfoForm()

    return render(request, 'recommendation_app/diet_recommendation_form.html', {'form': form, 'recommended_foods': recommended_foods})


def show_recommendation_form(request):
    if request.method == 'POST':
        # Get user input from the form

        goals = request.POST.get('goals')
        age = int(request.POST.get('age'))
        weight = float(request.POST.get('weight'))
        health_conditions = request.POST.get('health_conditions').split(',')

        # Call the genetic algorithm to get recommendations
        recommended_exercises = genetic_algorithm(goals, health_conditions)
        
        # Pass the recommendations to the template
        return render(request, 'recommendation_app/recommendation_result.html', {'recommended_exercises': recommended_exercises})

    # Render the form template for GET requests
    return render(request, 'recommendation_app/recommendation_form.html')


def ai_fitness_trainer(request):
    # Run your AI Fitness Trainer script using subprocess
    try:
        result = subprocess.run(["python", "/recommendation_app/ai_fitness_trainer.py"], capture_output=True, text=True)
        script_output = result.stdout
    except Exception as e:
        script_output = str(e)

    # You can pass the output or any other data to your template if needed
    context = {
        'script_output': script_output,
    }

    return render(request, 'recommendation_app/fitness_trainer.html', context)

def empty_favicon(request):
    return HttpResponse(status=204)

