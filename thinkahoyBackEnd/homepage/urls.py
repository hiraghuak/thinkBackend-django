from django.urls import path
from homepage import views

urlpatterns = [
    path('homepage/', views.homepageapi.as_view()),
]
