**Skill-Sharing Network**
Overview
The Skill-Sharing Network is a web application designed for college students to share and learn skills within their community. 
Students can register, list their skills, and connect with peers to exchange knowledge. 
The platform includes features like skill-sharing requests, profile management, and contact exchange.

Features
User Registration & Authentication:
Students can register and log in.
Profiles include skills, expertise, department, email, phone number, ID card number, and profile image.

Skill Search:
Students can search for peers based on skills or keywords.

Skill-Sharing Requests:
Students can send and accept skill-sharing requests.

Contact Exchange:
Contact details are exchanged when a request is accepted.

Profile Management:
Students can edit their profiles and upload images.

**Future Updates**
Feedback Mechanism:
Students will be able to provide feedback after skill-sharing sessions.
Feedback will influence search result rankings.

Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite (default), can be migrated to PostgreSQL or MySQL.
Media Storage: Local file storage for images (can be migrated to cloud storage like AWS S3).

Installation

Prerequisites
Python 3.x
Django 4.x
Git (optional)

Steps to Run the Project
Clone the Repository:

bash
git clone https://github.com/your-username/skill-sharing-network.git
cd skill-sharing-network
Create a Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
pip install -r requirements.txt

Run Migrations:

bash
python manage.py migrate
Create a Superuser (Admin):

bash
python manage.py createsuperuser
Run the Development Server:

bash
python manage.py runserver
Access the Application:

Open your browser and go to http://127.0.0.1:8000/.

Use the admin panel at http://127.0.0.1:8000/admin/ to manage data.

Project Structure
skill-sharing-network/
├── media/                  # Uploaded media files (e.g., profile images)
├── skill_sharing_network/  # Django project settings and configurations
├── students/               # Main app (user profiles, skill-sharing, feedback)
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── admin.py            # Admin configurations
│   ├── forms.py            # Forms for registration, profile editing, etc.
│   ├── models.py           # Database models (User, StudentProfile, SkillRequest, Feedback)
│   ├── urls.py             # App-specific URLs
│   └── views.py            # Views for handling requests and rendering templates
├── .gitignore              # Files and directories to ignore in Git
├── manage.py               # Django command-line utility
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
Usage
Register a New Account:

Go to the registration page (/register/) and fill in your details.

Upload a profile image (optional).

Log In:
Use your credentials to log in at /login/.

Search for Skills:
Use the search bar to find peers with specific skills.

Send Skill-Sharing Requests:
Visit a peer’s profile and send a request to learn a skill.

Accept/Decline Requests:
Go to the "View Requests" page (/view-requests/) to manage incoming requests.

Edit Your Profile:
Update your skills, expertise, and other details at /edit-profile/.

Contributing
Contributions are welcome! Follow these steps:
Fork the repository.
Create a new branch (git checkout -b feature/YourFeatureName).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeatureName).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, feel free to reach out:
Name: Udaykiran
Email: udaykiranu22@gmail.com
GitHub: udaykiranu22
