document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('authToken');
    const userRole = localStorage.getItem('role');
    const ticketList = document.getElementById('ticket-list');
    const logoutButton = document.getElementById('logout-button');

    // 1. Check for token and role
    // If no token, or if the user is not an agent/admin, redirect to login.
    if (!token || !['agent', 'admin'].includes(userRole)) {
        window.location.href = '/login/';
        return;
    }

    // 2. Fetch all tickets from the dedicated endpoint
    fetch('/api/tickets/all/', {
        method: 'GET',
        headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        // If token is invalid or user lacks permission, redirect to login
        if (response.status === 401 || response.status === 403) {
            localStorage.removeItem('authToken');
            localStorage.removeItem('role');
            window.location.href = '/login/';
            return;
        }
        return response.json();
    })
    .then(tickets => {
        if (!tickets || tickets.length === 0) {
            ticketList.innerHTML = '<tr><td colspan="5">No tickets found.</td></tr>';
            return;
        }

        // 3. Populate the table with ticket data
        tickets.forEach(ticket => {
            const row = document.createElement('tr');
            
            // Format date for better readability
            const createdAt = new Date(ticket.created_at).toLocaleString();

            row.innerHTML = `
                <td><a href="/ticket/${ticket.id}/">${ticket.subject}</a></td>
                <td>${ticket.status}</td>
                <td>${ticket.category ? ticket.category.name : 'N/A'}</td>
                <td>${ticket.created_by}</td>
                <td>${createdAt}</td>
            `;
            ticketList.appendChild(row);
        });
    })
    .catch(error => {
        console.error('Error fetching tickets:', error);
        ticketList.innerHTML = '<tr><td colspan="5">Failed to load tickets. Please try again later.</td></tr>';
    });

    // 4. Handle logout
    if (logoutButton) {
        logoutButton.addEventListener('click', () => {
            localStorage.removeItem('authToken');
            localStorage.removeItem('role');
            window.location.href = '/login/';
        });
    }
});