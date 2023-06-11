from django.urls import path
from . import views

urlpatterns = [
    path('rules/', views.RuleList.as_view()),
    path('rules/<int:pk>/', views.RuleDetail.as_view()),
]
