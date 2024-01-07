<template>
  <div>
    <div id="lista-cursos" class="container">
      <h1 id="encabezado" class="encabezado">Cursos En Línea</h1>
      <div class="row">
        <div class="three columns" v-for="curso in cursos" :key="curso.id">
          <div class="card">
            <img
              :src="curso.imagen"
              class="imagen-curso u-full-width"
              @click=""
            />
            <div class="info-card">
              <h4>{{ curso.nombre }}</h4>
              <p>{{ curso.autor }}</p>
              <img src="../img/estrellas.png" />
              <p class="precio">
                <p class="precio">{{ curso.precio }} <span class="u-pull-right">15€</span></p>
              </p>
              <button @click="verDetallesCurso(curso.id)">info</button>              
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
    this.obtenerCursos();
  },
  methods: {
    obtenerCursos() {
      axios
        .get("http://localhost:8000/api-cursos/cursos/")
        .then((response) => {
          this.cursos = response.data;
        })
        .catch((error) => {
          console.error("Error al obtener los cursos:", error);
        });
    },
    agregarAlCarrito(curso) {
      this.$emit("curso-agregado", curso);
    },
    verDetallesCurso(cursoId) {
      this.$router.push({ name: "detalles-curso", params: { id: cursoId } });
    },
  },
};
</script>
<style scoped>
/* Estilos para la tarjeta */
.card {
  position: relative;
}

/* Estilos para el botón 'info' */
.info-card button {
  position: absolute;
  top: 10px; /* Ajusta este valor para la distancia desde arriba */
  right: 10px; /* Ajusta este valor para la distancia desde la derecha */
  /* Otros estilos opcionales para el botón */
  background-color: #f1f1f1;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

</style>
