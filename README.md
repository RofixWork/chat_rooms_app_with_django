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
   git clone https://github.com/RofixWork/chat_rooms_app_with_django.git
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
### Register Page
![register](https://github.com/user-attachments/assets/1722819e-4ab7-4fe0-b9e7-e5ba5d261c35)

### Login Page
![login](https://github.com/user-attachments/assets/111172ac-0ebb-46ab-871e-8e0b7e244cda)

### Edit Profile Form
![editprofile](https://github.com/user-attachments/assets/12d0e39c-3b16-4550-aca9-0e6901a6a724)

### Home Page
![home2](https://github.com/user-attachments/assets/1471b980-c28f-4053-8e61-ff85c6e41819)

### Form for Add New Room
![aaddnewroom](https://github.com/user-attachments/assets/4891b86c-93a9-4a28-8aeb-28db30ad802d)

### Chat Room
![room_message](https://github.com/user-attachments/assets/01bf888d-7e33-4f2b-9b2b-5231dadda884)

### Real Time Chat (Websocket & ASGI)
![realtime](https://github.com/user-attachments/assets/071663d7-defb-4ea4-8633-4fbb71c1818c)

### Room Name already exist (because room_name is unique)
![raeady2](https://github.com/user-attachments/assets/a3e26bd9-ea23-4375-8897-b238eda761f8)

![ready2](https://github.com/user-attachments/assets/cc90b6bd-8c87-4a02-ae32-cc2a4f4c653a)


---

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License.

