# Library Management System

An open source Django project to manage library records data through Django built-in Admin Site.

***

## Technologies Used
  - Optimized Django Admin Panel
  - Django ORM
## Prerequisites
  - Python3
  
## Getting Started
First you will need to clone the repository:
  1) Create a new directory on your local machine or favourite code editor (VS Code, Atom etc...). I have called mine library. This is your "root directory".
  2) Go into the root directory and open a terminal right-clicking and holding Shift (if you're in Windows Explorer) or Ctrl + \`, then cd into the root directory (if you're in VS Code).
  3) You can now clone, using the command 'git clone' or using GitHub CLI (or alternatives as Git Bash):
  ```
  # option 1 - HTTPS
  git clone https://github.com/fismoilov20/library.git .
  
  # option 2 - Github CLI
  gh repo clone fismoilov20/library .
  ```
***

You should now have all files copied to your root directory (inside /library/ in my case). 
1) Virtual Environment – in the terminal (if you have already installed python virtual environment, if not run "pip install virtualenv" first) run the following commands to create a virtual environment:
```
python -m venv .venv
```

Then copy `.env.example` as `.env`:
```
# Windows
copy .env.example .env
# Linux, mac
cp .env.example .env
```

Now activate the virtual environment with the following command:
```
# Windows
venv\Scripts\activate

# mac/linux
source venv/bin/activate
```
You will know your virtual environment is active when your terminal displays the following:
```
(.venv) path\to\project\library>
```
## 

2) Packages and requirements - Our project will rely on django and python-decouple Python packages (requirements) to function. I have already created a requirements.txt file. So you can either run this command:
```
pip install -r requirements.txt
```
or install those two packages separately:
```
pip install django
```
and
```
pip install python-decouple
```
Now you're ready to launch the server. Use the following command to run the local server:
```
python manage.py runserver
```
You should see this log:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

November 05, 2022 - 12:18:44
Django version 4.1.3, using settings 'drf_course.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Now click on that link with Ctrl or Command to go to our local server website. The default login and password are 'user' and 'user' respectively. Further you can change the login credentials or add other users in the Admin Page's Users tab or some django built-in terminal commands, like:
```
python manage.py createsuperuser
```
– for creating another superuser.

***

In order to stop the local server just go to the terminal and press Crtl+C or Command+C.
Enjoy!!!


> Note: There's a comment in admin.py next to the line of code which fixes the following problem:

![GET BOOKS](https://user-images.githubusercontent.com/101515354/212142762-7986d7fd-2980-4591-aabd-cfd18bd3ac2f.png)


