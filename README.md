# Django Music Library

This is a Django-based digital music library where you can visualize artists and their albums, and open albums to view a description and list of songs. It also includes an autocomplete component for search functionality.

## Features

- List all artists, albums, and songs
- View album details and list of songs
- Search with autocomplete functionality
- Responsive design using Bootstrap


## Setup Instructions

### 1. Clone the Repository 
```bash
git clone https://github.com/yourusername/musiclibrary.git
cd musiclibrary 
```

### 2. Create a Virtual Environment
```bash
Create and activate a virtual environment:
python -m venv myenv
source myenv/bin/activate   # On macOS/Linux
myenv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create super user
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your web browser and go to http://127.0.0.1:8000/ to view the application.

### 8. Admin Interface
Access the admin interface to manage artists, albums, and songs:
```
http://127.0.0.1:8000/admin
```
