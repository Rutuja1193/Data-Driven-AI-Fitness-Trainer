from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homePage, name='index'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('signinup/', views.SignInUp, name='SignInUp'),
    path('help/', views.help, name='Help'),
    path('goals/', views.goals, name='Goals'),
     path('bmi_calculator/', views.bmi_calculator, name='BMI_calculator'),
     path('diet_recommendation_form', views.diet_recommendation_form, name='diet_recommendation_form'),
    path('recommendation_form/', views.show_recommendation_form, name='recommendation_form'),
    path('ai_fitness_trainer/', views.ai_fitness_trainer, name='ai_fitness_trainer'),
    path('favicon.ico', views.empty_favicon)
    # Add other URLs if needed
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
