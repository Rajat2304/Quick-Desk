# tickets/urls.py

from django.urls import path
# Import all the views used in this file, including the new one
from .views import (
    TicketListCreateView,
    TicketDetailView,
    CategoryListCreateView,
    CategoryDetailView,
    AllTicketsListView  # <-- This was the missing import
)

urlpatterns = [
    # Ticket URLs
    path('', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),

    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    # URL for the agent/admin view of all tickets
    path('all/', AllTicketsListView.as_view(), name='all-tickets-list'),
]
