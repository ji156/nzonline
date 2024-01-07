<template>
  <div>
    <Navbar
      :articulosCarritos="articulosCarritos"
      @eliminar-curso="eliminarCurso"
      @vaciar-carrito="vaciarCarrito"
    />
    <Principal />
    <Cursos @curso-agregado="agregarCursoAlCarrito" />
    <Footer />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Cursos from "./components/Cursos.vue";
import Principal from "./components/Principal.vue";
import Footer from "./components/Footer.vue";

export default {
  components: {
    Navbar,
    Cursos,
    Principal,
    Footer,
  },
  data() {
    return {
      articulosCarritos: [],
    };
  },
  methods: {
    eliminarCurso(cursoId) {
      this.articulosCarritos = this.articulosCarritos.filter(
        (curso) => curso.id !== cursoId
      );
    },
    vaciarCarrito() {
      this.articulosCarritos = [];
    },
    agregarCursoAlCarrito(curso) {
      const cursoEnCarrito = this.articulosCarritos.find(
        (c) => c.id === curso.id
      );
      if (cursoEnCarrito) {
        cursoEnCarrito.cantidad++; // Incrementa la cantidad si el curso ya está en el carrito
      } else {
        this.articulosCarritos.push({ ...curso, cantidad: 1 }); // Agrega el curso al carrito con cantidad 1 si no está en el carrito
      }
    },
  },
};
</script>

<style></style>
