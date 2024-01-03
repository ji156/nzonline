from django.urls import path, include
from rest_framework import routers
from cursos import views

router = routers.DefaultRouter()
router.register(r'cursos', views.CursosViewSet)

# Define las URL para la API de cursos
urlpatterns = [
    # http://localhost:8000/api-cursos/cursos/
    path('api-cursos/', include(router.urls)),
]
