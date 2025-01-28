# TODO_application

A simple and intuitive TODO application built using Django, allowing users to create, update, and delete tasks. Users can also mark tasks as completed and organize them by priority.

## Features

- User authentication (login/signup).
- Add, update, and delete tasks.
- Mark tasks as completed.
- Categorize tasks by priority (High, Medium, Low).
- Filter tasks by completion status and priority.
- Responsive UI built with Bootstrap.

## Technologies Used

- Django: Backend Framework.
- SQLite: Default database for local development.
- Bootstrap: Front-end framework for a responsive UI.
- HTML/CSS: Basic web design and styling.

## Prerequisites

- Python 3.x
- Django 3.x or higher
- Basic knowledge of Django and web development.

## Installation

### Step 1: CLone the repository

```bash
git clone https://github.com/shreya114/TODO_application.git
cd todo
```

### Step 2: Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run database migrations

```bash
python manage.py migrate
```

### Step 5: Run the development server

```bash
python manage.py runserver
```

## Usage

1. Open the app in your browser.
2. Sign up or log in if you already have an account.
3. Start adding your tasks!
4. Edit or delete tasks by clicking the respective buttons.
5. Filter tasks based on completion status or priority.
