Developers:
Akeziah Liezel A. Gonzaga, Lead Developer
Harvey A. Ortega
Ruliemhar Brian T. Gido

Project Managers:
Kurt David M. Monteclaro, Product Owner
Belden C. Medil Jr., Business Analyst
Matthew Rimar S. Martus, Scrum Master

📝 System Description
MentalEase is a mental health and wellness web application designed to help students track their moods, write journals, and access wellness resources. It also allows community engagement through anonymous posts and provides administrators tools to manage content and resources efficiently.

⚙️ Tech Stack
Frontend: Django Template (HTML, CSS, JS)
Backend: Django Framework (Python)
Database: Supabase / Firebase
Deployment: Vercel / Render
Version Control: GitHub

🚀 Features
👥 User Management
User Registration & Login (Email & Password)
Edit Profile Information
Upload Profile Picture
Reset Password via Email

Setup & run instructions

1. Fork the repository
	 Go to the MentalEase GitHub repository and click “Fork” to create your own copy.

2. Clone your forked repository

git clone https://github.com/Arvs013/CSIT327-G2-MentalEase.git
cd MentalEase-Project

command code . to direct your software 


3. Create a virtual environment

python -m venv env
env\Scripts\activate        # for Windows
# or
source env/bin/activate     # for macOS / Linux


4. Install the dependencies

pip install -r requirements.txt


(If requirements.txt is missing, run this instead:)

pip install django supabase python-dotenv djangorestframework


5. Set up environment variables

Create a file named .env in the root folder (same level as manage.py).

Add your Supabase credentials:

SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_KEY=<your-anon-key>


Do not share or upload this file.

6. Apply database migrations

python manage.py makemigrations
python manage.py migrate


7. Run the development server

python manage.py runserver


8. Access the app

Open http://127.0.0.1:8000/

Signup page: http://127.0.0.1:8000/students/signup/

Login page: http://127.0.0.1:8000/students/login/


9. Commit and push your updates

git add .
git commit -m "Your update message"
git push origin main

📊 Mood Tracking
Log daily moods using an emoji-based scale
View mood trends through interactive charts

📓 Journaling & Community
Private journaling module (CRUD)
Anonymous posting feature
Like and comment system on community posts

📚 Wellness Resources
View campus hotlines and mental health guides
Search and filter resources
Admin management for updating wellness content

🛠️ Admin Features
Moderate anonymous posts (approve/remove)
Manage wellness resources (CRUD)