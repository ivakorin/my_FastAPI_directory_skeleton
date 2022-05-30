# Моя структура каталогов FastAPI

## Скрипт создаёт структуру директорий для последующй работы

### Как пользоваться
Скачать скрипт, затем:
```shell
chmod +x fast_api_skeleton.py
```
```shell
./fast_api_skeleton.py
```
Вести путь до каталога с проектами, затем задать имя проекта. 

### Структура каталогов:
```
├── __init__.py
├── api
│  ├── __init__.py
│  └── api_v1
│     ├── __init__.py
│     └── endpoints
│        └── __init__.py
└── core
   └── __init__.py
   ├── crud
   │  └── __init__.py
   ├── db
   │  └── __init__.py
   ├── models
   │  └── __init__.py
   ├── schemas
   │  └── __init__.py
   ├── views
   │  └── __init__.py
   └── templates
       └── index.j2
```

