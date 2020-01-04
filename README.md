# cb_workshop
Carte Blanche workshop

**Steps to run this app**
- Extract the zip file
- After extracting move to the unzipped directory folder
- Install the external dependecies using pip
  ```
  python3 -m pip install -r requirements.txt (or) pip3 install -r requirements.txt
  ```
- Run database migrations using this command
  ```
  python3 manage.py migrate
  ```
- Run the app using the following command
  ```
  python3 manage.py runserver 0.0.0.0:8000
  ```

**Live demo**
- Install django && django-rest-framework

  ```
  python3 -m pip install django (or) pip3 install django
  ```
  ```
  python3 -m pip install djangorestframework (or) pip3 install djangorestframework
  ```
- Create a folder mydjango
  ```
  mkdir mydjango
  ```
- Create django project
  ```
  cd mydjango
  django-admin startproject sample
  ```
- Create django app
  ```
  cd sample 
  django-admin startapp webserver
  ```
- Open the sample/settings.py file and add the following lines at the end in INSTALLED_APPS list
  ```  
  INSTALLED_APPS = [
    ....,
    'rest_framework',
    'todos'
    ]
- Create webserver/urls.py file in webserver app
  ```
  
   
  
