from django.urls import path
from .views import calculator_view

app_name = "thermal"

urlpatterns = [
    path("", calculator_view, name="calculator"),
]
