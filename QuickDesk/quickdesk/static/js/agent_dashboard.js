// static/js/agent_dashboard.js
window.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('authToken');
    if (!token) {
        window.location.href = '/login/';
        return;
    }

    const ticketListDiv = document.getElementById('ticket-list');
    
    fetch('/api/tickets/all/', {
        headers: { 'Authorization': 'Token ' + token }
    })
    .then(response => {
        if (!response.ok) {
            // This will happen if a regular user tries to access this data
            throw new Error('Access Denied or Not Found');
        }
        return response.json();
    })
    .then(data => {
        ticketListDiv.innerHTML = ''; // Clear "Loading..."
        const ul = document.createElement('ul');
        if (data.length === 0) {
            ticketListDiv.innerHTML = '<p>There are no tickets in the system yet.</p>';
            return;
        }
        data.forEach(ticket => {
            const li = document.createElement('li');
            // This is the line that creates the link
            li.innerHTML = `<a href="/ticket/${ticket.id}/">ID: ${ticket.id} | User: ${ticket.created_by} | Subject: ${ticket.subject} | Status: ${ticket.status}</a>`;
            ul.appendChild(li);
        });
        ticketListDiv.appendChild(ul);
    })
    .catch(error => {
        console.error('Error:', error);
        // If there's an error (like access denied), send the user to their own dashboard
        window.location.href = '/dashboard/';
    });
});

document.getElementById('logout-button').addEventListener('click', function() {
    localStorage.removeItem('authToken');
    window.location.href = '/login/';
});
