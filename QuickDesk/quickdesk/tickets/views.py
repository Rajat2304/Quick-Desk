# tickets/views.py

from rest_framework import generics, permissions
from .models import Ticket, Category
from .serializers import TicketSerializer, CategorySerializer
from .permissions import IsOwnerOrAdminOrAgent, IsAdminOrAgent

# View for listing tickets or creating a new one
class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all tickets
        for the currently authenticated user.
        """
        return Ticket.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# View for retrieving, updating, or deleting a single ticket
class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrAdminOrAgent]

# View for listing categories or creating a new one (Admins only)
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

# View for retrieving, updating, or deleting a single category (Admins only)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class AllTicketsListView(generics.ListAPIView):
    """
    View to list all tickets in the system.
    Only accessible by Admin or Agent users.
    """
    queryset = Ticket.objects.all().order_by('-created_at') # Show newest first
    serializer_class = TicketSerializer
    permission_classes = [IsAdminOrAgent]
