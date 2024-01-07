<template>
  <div>
    <!-- Contenido del curso -->
    <h1>Este es el curso {{ curso.nombre }}</h1>
    <p>Autor: {{ curso.autor }}</p>
    <p>Precio: {{ curso.precio }}</p>
    <!-- Otros detalles del curso -->

    <!-- Estructura condicional para renderizar otros componentes -->
    <Navbar
      v-if="mostrarNavbar"
      :articulosCarritos="articulosCarritos"
      @eliminar-curso="eliminarCurso"
      @vaciar-carrito="vaciarCarrito"
    />
    <Principal v-if="mostrarPrincipal" />
    <Cursos v-if="mostrarCursos" @curso-agregado="agregarCursoAlCarrito" />
    <Footer v-if="mostrarFooter" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      curso: {}, // Almacena la información del curso actual
      // Variables para controlar la renderización de componentes
      mostrarNavbar: false,
      mostrarPrincipal: false,
      mostrarCursos: false,
      mostrarFooter: false,
    };
  },
  mounted() {
    // Obtener el ID del curso de los parámetros de la ruta
    const cursoId = this.$route.params.id;

    // Llamar a la API u obtener los detalles del curso por su ID
    axios
      .get(`http://localhost:8000/api-cursos/cursos/${cursoId}`)
      .then((response) => {
        this.curso = response.data; // Asignar los detalles del curso al objeto 'curso'
        // Cambiar el valor para mostrar/ocultar componentes
        this.mostrarNavbar = true;
        this.mostrarPrincipal = true;
        this.mostrarCursos = true;
        this.mostrarFooter = true;
      })
      .catch((error) => {
        console.error("Error al obtener los detalles del curso:", error);
      });
  },
};
</script>

<style>
/* Estilos opcionales para este componente */
</style>
