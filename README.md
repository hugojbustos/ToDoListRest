# ToDoListRest
Aplicación ToDo List(Lista de tareas) integrada con API REST

Proyecto Django realizando una ToDoList(lista de tareas) y agregando la funcionalidad de API REST

Instalación
pasos a seguir para la instalación de la aplicación:

$ pip install -r requirements.txt --timeout 120
Ahora construimos la Base de Datos para la aplicación Django, ejecutando los siguientes comandos:
$ python manage.py makemigrations
$ python manage.py migrate
Crear usuario administrador de Django
La apliación necesita el usuario administrador de Django para poder usar la misma.
Se recomienda usuario/contraseña root/root o admin/admin, no es necesario en esta aplicación una contraseña mas segura.

$ python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: your-user@mail.com
Password: 
Password (again): 
Superuser created successfully.

Una vez realizado el paso anterior ya estamos en condiciones de levantar el servidor para que corra la apalicación:

$ python manage.py runserver
Abra su navegador web con la siguiente URL: http://127.0.0.1:8000/admin y desde ahí podrá administrar todas las tareas que necesite.

Abra su navegador web con la siguiente URL: http://127.0.0.1:8000/tareas/ y de esa forma accediendo con, por ejemplo, el metodo GET.
Podría también consultar una tarea en particular por su ID indicadno en el browser http://127.0.0.1:8000/tareas/1, y de esta forma obtener
todos los datos de la tarea nro 1 como lo son su Id, Descripción, Estado y Adjunto(doc adjunto subido a la tarea)

Referencias:
Python/Django/DjangoRestFrameWork.
