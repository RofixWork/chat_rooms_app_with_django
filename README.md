# Chat Room Application

## Overview
This is a chat room application built using Django. It supports real-time messaging and provides an intuitive user experience with robust authentication and user profile management.

---

## Features

### Real-Time Messaging
- Set up WebSocket, Django Channels, and ASGI for real-time communication.

### Authentication
- **Register**: Users can sign up for an account.
- **Login**: Secure login system.
- **Logout**: Easy and secure logout functionality.

### User Profiles
- Each user has a profile with additional information:
  - Profile image
  - First name and last name
  - Phone number
  - City and country
- Users can edit their profile information.

### Room Management
- Users can:
  - Create chat rooms.
  - Delete chat rooms they own (along with all associated messages).

### Admin Panel Customization
- Customized admin panel using **Jazzmin**.
- Used **django-extensions** for additional management tools.

### Frontend
- Technologies used:
  - HTML
  - CSS
  - JavaScript
  - TailwindCSS
  - Flowbite Framework

---

## How It Works
- **Access Rooms**: Each chat room is accessible via a unique slug.
- **Send Messages**: Any user can send messages in a room.
- **Real-Time Updates**: All users in the room see messages instantly due to the implementation of Django Channels and WebSocket consumers.

---

## Installation

### Prerequisites
1. Python installed (>=3.8).
2. Django installed (>=4.0).
3. Node.js for frontend tooling (optional, for TailwindCSS and Flowbite).

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Open the application in your browser at `http://127.0.0.1:8000/`.

---

## Screenshots
_Add relevant screenshots of the application interface here._

---

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License.

