from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    # Make created_by read-only because it will be set automatically based on the logged-in user.
    created_by = serializers.ReadOnlyField(source='created_by.username')
    # Optionally, display the username for assigned_to as well.
    assigned_to = serializers.ReadOnlyField(source='assigned_to.username', allow_null=True)

    class Meta:
        model = Ticket
        fields = ['id', 'subject', 'description', 'status', 'created_by', 'assigned_to', 'created_at', 'updated_at']