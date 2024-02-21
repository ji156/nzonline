# Plataforma de Cursos Online

## Descripción

Este proyecto es una plataforma de cursos online que permite a los usuarios acceder a una variedad de cursos sobre diferentes temas. Los usuarios pueden inscribirse, ver detalles de los cursos, acceder al material del curso y más.

## Características

- **Catálogo de Cursos:** Explora una amplia gama de cursos sobre varios temas.
- **Detalles del Curso:** Mira detalles como la descripción, el precio, la duración y el autor del curso.
- **Inscripción:** Regístrate y accede a cursos en los que estás interesado.
- **Material del Curso:** Accede a material educativo como videos, presentaciones, documentos, etc.
- **Calificación y Comentarios:** Comparte tu opinión sobre el curso y califícalo.

## Tecnologías Utilizadas

- **Frontend:** HTML, CSS, JavaScript, Vue.js
- **Backend:** Django, Django REST Framework
- **Base de Datos:** SQLite (para desarrollo), PostgreSQL (para producción)
- **Otros:** Axios, CORS para manejar solicitudes de dominios cruzados.

## Instalación

1. Clona este repositorio: `git clone https://github.com/ji156/nzonline.git`
2. Entra en la carpeta clonada: `cd nzonline` 
3. Configura el entorno virtual: `python3 -m venv venv`
4. Activa el entorno virtual: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
5. Instala las dependencias: `pip install -r requirements.txt`
6. Entra en la carpeta backend: `cd backend`
7. Ejecuta las migraciones: `python3 manage.py makemigrations` `python manage.py migrate`
8. Si queremos crear un superusuario para entrar al admin de django: `python3 manage.py createsuperuser` 
8. Inicia el servidor: `python3 manage.py runserver`
9. Regresa al directorio anterior: `cd ..`
10. Entra en la carpeta nz-online: `cd nz-online`
11. Ejecuta vite en modo dev: `npm run dev`
(Si aparece un error instalamos vite: `npm install vite --save-dev`)
12. Ahora podemos entrar en localhost:5173 (frontend) o localhost:8000/admin(backend)

## Uso

- Accede a la plataforma desde tu navegador: `http://localhost:5173`
- Accede al admin backend desde tu navegador: `http://localhost:5173`
- Explora el catálogo de cursos, inscríbete en los que te interesen y disfruta del material educativo.

