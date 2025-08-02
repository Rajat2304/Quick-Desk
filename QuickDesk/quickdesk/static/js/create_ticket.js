// static/js/create_ticket.js

const ticketForm = document.getElementById('create-ticket-form');
const messageDiv = document.getElementById('message');

ticketForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const subject = event.target.subject.value;
    const description = event.target.description.value;
    const token = localStorage.getItem('authToken');

    if (!token) {
        window.location.href = '/login/';
        return;
    }

    fetch('/api/tickets/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        },
        body: JSON.stringify({
            subject: subject,
            description: description
        })
    })
    .then(response => {
        if (response.ok) {
            // If the ticket was created successfully, redirect to the dashboard
            window.location.href = '/dashboard/';
        } else {
            // If there was an error, display it
            return response.json().then(data => {
                messageDiv.innerHTML = 'Error: ' + (data.detail || 'Could not create ticket.');
                messageDiv.style.color = 'red';
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        messageDiv.innerHTML = 'An error occurred. Please try again.';
        messageDiv.style.color = 'red';
    });
});
