from django.contrib import admin
from .models import Ticket

# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'status', 'created_by', 'assigned_to', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('subject', 'description', 'created_by__username')
    raw_id_fields = ('created_by', 'assigned_to')
