# Virtual Environment (venv)
# - environment which help us to execute our django project easily
# including dependencies that are speific to a particular django project 
# keeping it separate from the other project
# create venv ->  py -m venv example1_env
# activate the venv-> cd example1_env/Scripts -> activate
# deactivate the activated venv -> deactivate



# PIP - Package Manager
# - pre-defined / in-built packages 
# - custom packages 
# - third-party packages 
# pip --version - included in Python (3.12)
#  - modularity, separation of concerns
#  - package management - manages the versions of the pyhton packages
#  - dependency management - manages the versions of 3rd party libraries and frameworks

# Download the framework -> py -m pip install Django
# Check version of Django downloaded -> django-admin --version

# Create Project: example1_project
#  -> django-admin startproject example1_project
#  -> cd example1_project 
#  -> py manage.py runserver

# Apps
# Travel Management System - visa, destinations, flights, trip package, booking, 
#                           customers, report .....
# server should be up and running
# -> py manage.py startapp destinations
# -> in settings.py file -> add the app in INSTALLED_APPS as string

# Shut down the server -> ctrl+C
