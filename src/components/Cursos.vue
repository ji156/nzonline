<template>
  <div class="container">
    <ul>
      <li v-for="curso in cursos" :key="curso.id" class="cursos">
        <div>
          <h3>{{ curso.nombre }}</h3>
          <p>Precio: {{ curso.precio }}</p>
          <p>Oferta: {{ curso.precio_oferta }}</p>
          <p>Categoría: {{ curso.categoria }}</p>
          <img
            :src="curso.imagen"
            alt="Imagen del curso"
            style="max-width: 200px; max-height: 200px"
          />
        </div>
      </li>
    </ul>
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
  created() {
    axios
      .get("http://localhost:8000/api-cursos/cursos/")
      .then((response) => {
        this.cursos = response.data;
      })
      .catch((error) => {
        console.error("Error al obtener los datos:", error);
      });
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.cursos {
  list-style: none;
  padding: 10px;
  margin: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
