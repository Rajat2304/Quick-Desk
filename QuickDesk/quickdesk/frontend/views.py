# frontend/views.py

from django.shortcuts import render

# View for the main login page
def login_page(request):
    return render(request, 'login.html')

# View for the regular user dashboard
def dashboard_page(request):
    return render(request, 'dashboard.html')
    
# View for the "Create Ticket" page
def create_ticket_page(request):
    return render(request, 'create_ticket.html')

# This is the view that was missing
# View for the agent/admin dashboard
def agent_dashboard_page(request):
    return render(request, 'agent_dashboard.html')

def ticket_detail_page(request, pk):
    # We pass the pk to the template, but we won't use it there.
    # The JavaScript will get the pk from the URL.
    return render(request, 'ticket_detail.html')

