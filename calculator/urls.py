from django.urls import path
from .views import calculator_view, calculator_detail_view as cdv

app_name = "thermal"

urlpatterns = [
    path("", calculator_view, name="calculator"),
    path("<int:pk>/", cdv, name="detail"),
]
