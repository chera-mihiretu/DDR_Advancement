from django.urls import path
from . import views
urlpatterns = [
    path('', views.showQuestion),
    path('<int:question_id>/', views.detail),
    path('<int:question_id>/result/', views.result),
]