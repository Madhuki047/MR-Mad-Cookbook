# MR Mad CookBook (In Progress)

A Django-based recipe management web app with categories, search, and a clean, extensible architecture.  
Future plans include integrating machine learning for personalised recommendations.


## Overview

MR Mad CookBook is a full-stack **Django** application for organising and browsing recipes.

The focus of this version is:

- A **clear data model** for recipes and categories  
- A simple, intuitive **UI using Django templates + Bootstrap**  
- A solid foundation that can later be extended with APIs and ML features

The app is built as a **monolithic, server-rendered Django project**:  
Django handles URL routing, the ORM, business logic in views, and HTML rendering.


## Features

- **Categories** (e.g. British, Sri Lankan, Italian, Chinese)
- **Recipes** with:
  - ingredients  
  - step-by-step instructions  
  - difficulty level  
  - prep & cook time  
- **Search** on recipe titles  
- **Slug-based URLs** for recipes and categories  
- **Django admin** for quick data management  
- Clean separation of:
  - `models.py` – data layer  
  - `views.py` – request handling & business logic  
  - `templates/` – presentation layer


## Tech Stack

- Backend : Python 3, Django
- Frontend: Django Templates, Bootstrap 5
- Database: SQLite (development)
- Tools   : Git, GitHub  

## Live Demo
http://127.0.0.1:8000/
![Screenshot 1 - Home page](https://raw.githubusercontent.com/Madhuki047/MR-Mad-Cookbook/main/Screenshot%20(338).png)
![Screenshot 2 - All recipes page](https://raw.githubusercontent.com/Madhuki047/MR-Mad-Cookbook/main/Screenshot%20(339).png)
![Screenshot 3 - Categories page](https://raw.githubusercontent.com/Madhuki047/MR-Mad-Cookbook/main/Screenshot%20(340).png)
