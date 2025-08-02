# frontend/urls.py

# frontend/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('dashboard/', views.dashboard_page, name='dashboard_page'),
    path('create-ticket/', views.create_ticket_page, name='create_ticket_page'),
    
    # Add the agent dashboard URL here, in the correct file
    path('agent/dashboard/', views.agent_dashboard_page, name='agent_dashboard_page'),
    path('ticket/<int:pk>/', views.ticket_detail_page, name='ticket_detail_page'),
]
