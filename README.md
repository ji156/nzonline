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
- **Otros:** Axios, JWT para autenticación, CORS para manejar solicitudes de dominios cruzados.

## Instalación

1. Clona este repositorio: `git clone https://github.com/ji156/nzonline.git`
2. Configura el entorno virtual: `python -m venv venv`
3. Activa el entorno virtual: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta las migraciones: `python manage.py migrate`
6. Inicia el servidor: `python manage.py runserver`

## Uso

- Accede a la plataforma desde tu navegador: `http://localhost:8000`
- Explora el catálogo de cursos, inscríbete en los que te interesen y disfruta del material educativo.

## Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir un pull request para sugerir mejoras, correcciones de errores o nuevas características.

## Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).
