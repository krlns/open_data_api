from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('cinema/', views.CinemaList.as_view()),
    path('cinema/<int:pk>/', views.CinemaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
