// static/js/ticket_detail.js

window.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('authToken');
    if (!token) {
        window.location.href = '/login/';
        return;
    }

    const pathParts = window.location.pathname.split('/');
    const ticketId = pathParts[2];

    // Fetch ticket details when the page loads
    fetch(`/api/tickets/${ticketId}/`, {
        headers: { 'Authorization': 'Token ' + token }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('ticket-subject').textContent = data.subject;
        document.getElementById('ticket-status').textContent = data.status;
        document.getElementById('ticket-creator').textContent = data.created_by;
        document.getElementById('ticket-created-at').textContent = new Date(data.created_at).toLocaleString();
        document.getElementById('ticket-description').textContent = data.description;
        
        // Set the dropdown to the ticket's current status
        document.getElementById('status-select').value = data.status;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Could not load ticket details.');
    });

    // --- THIS IS THE NEW PART WE ARE ADDING ---

    // Handle the form submission for updating the status
    const updateForm = document.getElementById('update-status-form');
    const updateMessageDiv = document.getElementById('update-message');

    updateForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const newStatus = document.getElementById('status-select').value;

        // Send a PATCH request to update only the status field
        fetch(`/api/tickets/${ticketId}/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + token
            },
            body: JSON.stringify({ status: newStatus })
        })
        .then(response => response.json())
        .then(data => {
            // Update the status on the page and show a success message
            document.getElementById('ticket-status').textContent = data.status;
            updateMessageDiv.textContent = 'Status updated successfully!';
            updateMessageDiv.style.color = 'green';
        })
        .catch(error => {
            console.error('Error updating status:', error);
            updateMessageDiv.textContent = 'Failed to update status.';
            updateMessageDiv.style.color = 'red';
        });
    });
});
