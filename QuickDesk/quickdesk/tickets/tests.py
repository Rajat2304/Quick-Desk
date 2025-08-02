from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser
from .models import Ticket

class TicketAPITests(APITestCase):
    def setUp(self):
        """
        Set up the test environment.
        This method is called before each test.
        """
        self.end_user = CustomUser.objects.create_user(
            username='testuser',
            password='password123',
            role='end_user'
        )
        # Log in the end_user for most tests
        self.client.force_authenticate(user=self.end_user)

        # Create a sample ticket for detail/update/delete tests
        self.ticket = Ticket.objects.create(
            subject="Initial Test Ticket",
            description="A description for the test ticket.",
            created_by=self.end_user
        )

    def test_create_ticket_authenticated(self):
        """
        Ensure an authenticated user can create a new ticket.
        """
        url = reverse('ticket-list-create')
        data = {'subject': 'New API Ticket', 'description': 'Help me with the API.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 2) # 1 from setUp, 1 from this test
        # Check that the creator is the logged-in user
        new_ticket = Ticket.objects.get(id=response.data['id'])
        self.assertEqual(new_ticket.created_by, self.end_user)

    def test_create_ticket_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create a ticket.
        """
        self.client.force_authenticate(user=None) # Log out
        url = reverse('ticket-list-create')
        data = {'subject': 'Unauthorized Ticket', 'description': 'This should fail.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_tickets(self):
        """
        Ensure an authenticated user can list tickets.
        """
        url = reverse('ticket-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_ticket(self):
        """
        Ensure an authenticated user can retrieve a specific ticket.
        """
        url = reverse('ticket-detail', kwargs={'pk': self.ticket.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject'], self.ticket.subject)

    def test_update_ticket(self):
        """
        Ensure an authenticated user can update a ticket.
        """
        url = reverse('ticket-detail', kwargs={'pk': self.ticket.pk})
        updated_data = {'subject': 'Updated Subject', 'status': 'In Progress'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ticket.refresh_from_db()
        self.assertEqual(self.ticket.subject, 'Updated Subject')

    def test_delete_ticket(self):
        """
        Ensure an authenticated user can delete a ticket.
        """
        url = reverse('ticket-detail', kwargs={'pk': self.ticket.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ticket.objects.count(), 0)
