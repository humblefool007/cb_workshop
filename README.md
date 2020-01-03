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
