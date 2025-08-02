# Quick-Desk


QuickDesk is a web-based help desk ticketing system built with Django and the Django REST Framework. It provides a RESTful API for managing users, tickets, and categories, along with a simple frontend interface for interaction. The system features role-based access control, distinguishing between end-users, support agents, and administrators.

Features
User Authentication: Secure user registration and token-based login system.

Role-Based Access Control (RBAC):

End-User: Can create tickets and view their own tickets.

Agent: Can view all tickets, update their status, and assign tickets to themselves.

Admin: Has full access, including category management and staff-level ticket viewing.

Ticket Management:

Users can create, view, and update their own tickets from a dedicated dashboard.

Agents have a separate dashboard to view and manage all tickets in the system.

Category Management: Admins can create and manage categories for organizing tickets.

RESTful API: A clean and powerful API for all core functionalities, built with Django REST Framework.

Simple Frontend: A lightweight frontend built with HTML, CSS, and vanilla JavaScript that interacts with the backend API.

Technology Stack
Backend: Python, Django, Django REST Framework

Database: SQLite 3 (default)

Frontend: HTML, CSS, Vanilla JavaScript

Setup and Installation
Follow these steps to set up and run the project locally.

1. Prerequisites
Python 3.8+

pip (Python package installer)

2. Clone the Repository
bash
git clone https://github.com/Rajat2304/quickdesk.git
cd QuickDesk


3. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

On Windows:

bash
python -m venv venv
.\venv\Scripts\activate
On macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
Install all the required packages using the requirements.txt file.

bash
pip install -r requirements.txt
5. Apply Database Migrations
This command will create the necessary database tables based on your models.

bash
python manage.py migrate
6. Create a Superuser
You will need a superuser (admin) account to access the admin panel and test agent/admin features.

bash
python manage.py createsuperuser
Follow the prompts to create your admin username and password.

Running the Application
Once the setup is complete, you can run the development server:

bash
python manage.py runserver
The application will be available at http://127.0.0.1:8000/.

How to Use
1. Accessing the Frontend
Login Page: Navigate to http://127.0.0.1:8000/login/ in your web browser.

2. Creating Test Users
You will need to create an agent and an end_user to test the role-based features. Use an API client like Postman or Insomnia to send POST requests to the registration endpoint: http://127.0.0.1:8000/api/accounts/register/.

Create an Agent:

json
{
    "username": "testagent",
    "email": "agent@example.com",
    "password": "password123",
    "role": "agent"
}
Create an End-User:

json
{
    "username": "testuser",
    "email": "user@example.com",
    "password": "password123",
    "role": "end_user"
}
You can now log in with these users on the login page to see their respective dashboards.
