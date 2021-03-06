import os
import sys

project_name = sys.argv[1]
templates_folder = sys.argv[2]

try:
    os.system(f"cd Destination && django-admin startproject {project_name}")
    print(f"{project_name} structure has build..")
except:
    print("  ERROR : Unable to make Django project")
    exit(1)

# making templates directory withing django project
try:
    os.system(f"cd Destination\{project_name} && mkdir {templates_folder}")
    print(f"{templates_folder} directory has build..")
except:
    print("  ERROR : Unable to make templates directory")
    exit(1)

# making the initial django_site page for render
try:
    os.system(f"python routjango\initial_site.py {project_name} {templates_folder}")
    print(f"inital django_site.html has build..")
except:
    print("  ERROR : Unable to call routjango\initial_site.py file")
    exit(1)

# # making srv app withing the django project
try:
    os.system(f"python routjango\srv_init.py {project_name}")
    print(f"app in the {project_name} has build..")
except:
    print("  ERROR : Unable to call routjango\srv_init.py file")
    exit(1)

# adding srv-app and templates folder in the danago project setting.py
try: 
    os.system(f"python routjango\setting_main.py {project_name} {templates_folder}")
    print(f"setting has build for templates and app..")
except:
    print("  ERROR : Unable to call routjango\setting_main.py file")
    exit(1)


# adding srv-urls.py in the danago project urls.py
try: 
    filename = "urls"
    os.system(f"python routjango\{filename}_main.py {project_name}")
    print(f"route(urls) file has build..")
except:
    print(f"  ERROR : Unable to call routjango\{filename}_main.py file")
    exit(1)

# doing migration
try:
    os.system(f"cd Destination\{project_name} && python manage.py migrate")
    print(f"initial migration has done..")
except:
    print(f"  ERROR: Unable to make initial migration")



