<template>
  <div>
    <!-- Lista de cursos -->
    <div id="lista-cursos" class="container">
      <h1 id="encabezado" class="encabezado">Cursos En Línea</h1>
      <div class="row">
        <div class="four columns" v-for="curso in cursos" :key="curso.id">
          <div class="card">
            <img
              :src="curso.imagen"
              class="imagen-curso u-full-width"
              @click=""
            />
            <div class="info-card">
              <h4>{{ curso.titulo }}</h4>
              <p>{{ curso.instructor }}</p>
              <img src="../img/estrellas.png" />
              <p class="precio">$200 <span class="u-pull-right">$15</span></p>
              <a
                href="#"
                class="u-full-width button-primary button input agregar-carrito"
                @click="agregarAlCarrito(curso)"
                >Agregar Al Carrito</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      cursos: [],
    };
  },
  mounted() {
    // Hacer la solicitud HTTP para obtener los cursos
    this.obtenerCursos();
  },
  methods: {
    obtenerCursos() {
      // Realizar la solicitud GET a la API para obtener los cursos
      axios
        .get("http://localhost:8000/api-cursos/cursos/")
        .then((response) => {
          // Asignar los cursos obtenidos de la API a la variable 'cursos'
          this.cursos = response.data;
        })
        .catch((error) => {
          console.error("Error al obtener los cursos:", error);
        });
    },
  },
};
</script>

<style>
/* Estilos opcionales para este componente */
</style>
