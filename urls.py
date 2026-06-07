from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('dashboard/', views.dashboard),
    path('diet/', views.diet),
    path('exercise/', views.exercise),
    path('water/', views.water),
    path('bmi/', views.bmi),
    path('recommendation/', views.recommendation),
    path('about/', views.about),
    path('login/', views.login_page),
    path('signup/', views.signup_page),
]