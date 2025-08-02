# Quick-Desk


🚀 QuickDesk: A Modern Help Desk System
A powerful, role-based help desk ticketing system built with Django and Django REST Framework. Designed for simplicity and functionality, QuickDesk provides a complete solution for managing support tickets for users, agents, and administrators.

✨ Table of Contents
Key Features :
Technology Stack
Setup and Installation
Running the Application
How to Test the System
Project Structure

🌟 Key Features
🔑 Secure Authentication: Robust user registration and token-based login.
👤 Role-Based Dashboards:
End-Users: A clean dashboard to view their tickets and create new ones.
Agents/Admins: A powerful dashboard to view all tickets, update status, and assign ownership.
🎫 Advanced Ticket Management: Create, view, update, and assign tickets with ease.
🗂️ Dynamic Category System: Admins can manage ticket categories to keep things organized.
🔌 RESTful API: A well-structured API built with Django REST Framework for all core actions.
🖥️ Lightweight Frontend: A simple and responsive user interface built with vanilla JavaScript that communicates with the backend.

💻 Technology Stack
Backend: Python, Django, Django REST Framework
Database: SQLite 3 (default)
Frontend: HTML5, CSS3, Vanilla JavaScript
⚙️ Setup and Installation
Follow these steps to get a local copy up and running.

1. Prerequisites
Python 3.8 or higher
pip and venv
2. Clone the Repository
Clone this repository to your local machine.
git clone https://github.com/Rajat2304/quickdesk.git
cd quickdesk
3. Create and Activate a Virtual Environment
Using a virtual environment is a best practice for managing dependencies.
bash
# Create a virtual environment
python -m venv venv
# Activate it (Windows)
.\venv\Scripts\activate
# Activate it (macOS/Linux)
source venv/bin/activate
4. Install Dependencies
Install all required packages from the requirements.txt file.
bash
pip install -r requirements.txt
5. Run Database Migrations
This creates the necessary database schema for your application.
bash
python manage.py migrate
6. Create a Superuser
This account will have admin privileges, allowing you to test the agent/admin dashboard.
bash
python manage.py createsuperuser
Follow the prompts to set your username, email, and password.

🏃 Running the Application
Start the Django development server with this command:
bash
python manage.py runserver
The application is now live! Visit http://127.0.0.1:8000/login/ in your web browser.

🧪 How to Test the System
To fully experience the role-based features, you need to create different types of users. Use an API client like Postman or Insomnia to send POST requests to the registration endpoint: http://127.0.0.1:8000/api/accounts/register/.

<details> <summary><b>Click to see Agent creation payload</b></summary>
json
{
    "username": "testagent",
    "email": "agent@example.com",
    "password": "password123",
    "role": "agent"
}
</details> <details> <summary><b>Click to see End-User creation payload</b></summary>
json
{
    "username": "testuser",
    "email": "user@example.com",
    "password": "password123",
    "role": "end_user"
}
</details>
After creating the users, log in with their credentials on the login page to access their respective dashboards.


📂 Project Structure
A brief overview of the project's layout:

text
QuickDesk/
├── accounts/          # Handles user registration and authentication
├── frontend/          # Serves the HTML templates and frontend logic
├── tickets/           # Manages tickets, categories, and API views
├── static/            # Contains all static files (CSS, JS)
│   ├── css/
│   └── js/
├── templates/         # Contains all HTML files
├── quickdesk/         # Main project configuration (settings.py, urls.py)
├── db.sqlite3         # The project's database file
├── manage.py          # Django's command-line utility
└── requirements.txt   # List of Python dependencies


