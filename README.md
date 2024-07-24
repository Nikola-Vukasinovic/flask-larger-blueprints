# Demo project refactoring existing project with blueprints

## Refactoring with Flask Blueprints to accomodate for project scaling

### Requirements

Python version >= 3.6

Please use provided **requirements.txt** for needed package installation with:

```
pip install -p requirements.txt
```

### **Project upgrade**

This project is actually an refactor and update effort on the existing project that can be found [Nikola-Vukasinovic/flask-sql-project](https://github.com/Nikola-Vukasinovic/flask-sql-project "Linked project") by utilizing Blueprints.

### **Project structure**

Please note following project structure:

Under root folder there is app.py that is entry level into html view structure.

Migrations folder is also under root when using Migrate and SQLAlchemy.

Application root folder is **adoption_site** and contains folders for different *modules* of the web app in line with SOLID principles (or at least an effort in that direction).

Notice that each web app module has following structure <module_name>/templates/<module_name>. Altough it seems redundant this is as per Blueprints design best practices. Each app module has also *forms.py* and *views.py*.

More examples and materials for using Blueprints can be found on:

[Real Python Blueprints](https://realpython.com/flask-blueprint/ "Flask Blueprints")

[Flask Blueprints](https://flask.palletsprojects.com/en/3.0.x/blueprints/ "Flask Blueprints")

NOTE:

For database deletion and app setup see [DB &amp; App setup](https://github.com/Nikola-Vukasinovic/flask-sql-project#database-setup "Setup").
