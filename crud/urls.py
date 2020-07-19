from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_or_create),
    path('<int:id>/', views.update_or_delete)
]
