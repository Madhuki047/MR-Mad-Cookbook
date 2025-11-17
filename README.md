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

- **Categories** (e.g. Breakfast, Dessert, Vegan)
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

- Python 3  
- Django  
- SQLite (development)  
- Bootstrap 5 (CDN)  


## Project Structure

```text
MR-Mad-Cookbook/
├─ manage.py
├─ mrmad_cookbook/        # Project config: settings, urls, WSGI/ASGI
└─ recipes/               # Core app: models, views, templates
   └─ templates/recipes/  # base.html, home, lists, details
