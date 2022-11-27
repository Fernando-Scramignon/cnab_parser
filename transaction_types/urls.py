from django.urls import path
from . import views


urlpatterns = [path("transaction_types/", views.TransactionTypeView.as_view())]
