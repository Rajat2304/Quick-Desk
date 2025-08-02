// static/js/login.js
const loginForm = document.getElementById('login-form');
const messageDiv = document.getElementById('message');

loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const username = event.target.username.value;
    const password = event.target.password.value;

    fetch('/api/accounts/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            // Store both the token and the user's role
            localStorage.setItem('authToken', data.token);
            localStorage.setItem('role', data.role);

            // Correctly redirect based on the role
            if (data.role === 'admin' || data.role === 'agent') {
                window.location.href = '/agent/dashboard/';
            } else {
                window.location.href = '/dashboard/';
            }
        } else {
            messageDiv.innerHTML = 'Login Failed: ' + (data.error || 'Unknown error');
            messageDiv.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        messageDiv.innerHTML = 'An error occurred during login.';
        messageDiv.style.color = 'red';
    });
});
