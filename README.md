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
    'webserver'
    ]
- Create webserver/urls.py file in webserver app
  ```
  from django.urls import path
  from .views import hello

  urlpatterns = [
    path("hello", hello)
   ]
   ```
- Create webserver/views.py file in 
  ```
  from rest_framework.response import Response
  from rest_framework.decorators import api_view
  
  @api_view(["GET"])
  def hello(request):
      return Response({"message": "hello world"}, status=200)
   ```
- Edit sample/urls.py file in
  ```
  from django.contrib import admin
  from django.urls import path
  from django.urls import include

  urlpatterns = [
      path('apis/v1/', include('webserver.urls')),
  ]
  ```
- Run the webserver 
  ```
  python3.6 manage.py startserver
  ```

  
