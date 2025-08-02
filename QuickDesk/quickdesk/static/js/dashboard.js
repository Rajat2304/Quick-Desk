// static/js/dashboard.js
const ticketListDiv = document.getElementById('ticket-list');
const logoutButton = document.getElementById('logout-button');

window.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('authToken');
    if (!token) {
        window.location.href = '/login/';
        return;
    }

    fetch('/api/tickets/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        }
    })
    .then(response => response.json())
    .then(data => {
        ticketListDiv.innerHTML = ''; 
        if (data.length === 0) {
            ticketListDiv.innerHTML = '<p>You have not created any tickets yet.</p>';
        } else {
            const ul = document.createElement('ul');
            data.forEach(ticket => {
                const li = document.createElement('li');
                li.textContent = `ID: ${ticket.id} - Subject: ${ticket.subject} (Status: ${ticket.status})`;
                ul.appendChild(li);
            });
            ticketListDiv.appendChild(ul);
        }
    })
    .catch(error => {
        console.error('Error fetching tickets:', error);
        ticketListDiv.innerHTML = '<p>Could not load tickets.</p>';
    });
});

logoutButton.addEventListener('click', function() {
    localStorage.removeItem('authToken');
    window.location.href = '/login/';
});

