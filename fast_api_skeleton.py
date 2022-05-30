import os

print("""
FastAPI project sceleton
Usual project structure
├── Your app name
│  ├── __init__.py
│  ├── api
│  │  ├── __init__.py
│  │  └── api_v1
│  │     ├── __init__.py
│  │     └── endpoints
│  │        └── __init__.py
│  ├── core
│  │  └── __init__.py
│  ├── crud
│  │  └── __init__.py
│  ├── db
│  │  └── __init__.py
│  ├── models
│  │  └── __init__.py
│  ├── schemas
│  │  └── __init__.py
│  └── templates
│     └── index.j2
""")

path = input('Put full path here: ')
project_name = input('Put project name here: ')
dirs = ['api', 'api/api_v1', 'api/api_v1/endpoints', 'core', 'crud',
            'db', ' models', 'schemas', 'tests', 'templates', 'views']
for directory in dirs:
    full_path = os.path.join(path, project_name, directory)
    try:
        os.makedirs(full_path)
    except FileExistsError:
        print('Dirrectory exist, please check and try again')
        exit(1)
    if directory == 'templates':
        open(os.path.join(full_path, 'index.j2'), 'a').close()
    else:
        open(os.path.join(full_path, '__init__.py'), 'a').close()
full_path = os.path.join(path, project_name)
print(f"Project sceleton has been created for follow path {full_path}")
exit(0)
