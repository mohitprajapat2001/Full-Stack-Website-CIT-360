Apologies for the oversight. Here's the revised version of the `README.md` file that includes your name as the creator:

```markdown
# CIT 360 - Full Stack Website Project

Welcome to the CIT 360 project repository! This repository contains the source code and project documentation for a Full Stack website developed by Mohit Prajapat. The project was built using Python, Django Web Framework, HTML, CSS, JavaScript, jQuery, Bootstrap, and Git Version Control System.

## Project Overview

CIT 360 is a Full Stack website project aimed at providing a centralized platform for students and teachers to access academic resources, communicate with each other, and share information. The website includes features like UI/UX Designing, Website Admin Panel, Separate Student and Teachers Login, Certificate Downloads, Campaign app, Chat Bot, and Suggestion Tabs for Internships and Updates.

## Getting Started

To get a local copy of the project up and running on your machine, follow the steps below.

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your machine:

- Python 
- Django 
- PostgreSQL 
- Git

### Installation

1. Clone the repository:

```shell
git clone https://github.com/mohitprajapat2001/Full-Stack-Website-CIT-360
```

2. Navigate to the project directory:

```shell
cd cit-360-project
```

3. Install the project dependencies:

```shell
pip install -r requirements.txt
```

4. Create a PostgreSQL database for the project.

5. Configure the database settings:
   - Open the `settings.py` file located in the `cit360` directory.
   - Update the `DATABASES` configuration with your PostgreSQL database details.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

6. Apply database migrations:

```shell
python manage.py migrate
```

## Usage

To run the project locally, execute the following command:

```shell
python manage.py runserver
```

The website will be accessible at `http://localhost:8000` in your web browser.

## Contributing

Contributions to the CIT 360 project are welcome! If you have any improvements or new features to propose, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes and push the branch to your forked repository.
4. Submit a pull request detailing your changes.

## License

This project is licensed under the [MIT License](LICENSE).
```
