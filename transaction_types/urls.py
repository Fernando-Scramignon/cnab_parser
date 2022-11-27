from django.urls import path
from . import views


urlpatterns = [
    path("transaction_types/", views.TransactionTypeView.as_view()),
    path("transaction_types/<str:pk>/", views.TransactionTypeDetailView.as_view()),
]
