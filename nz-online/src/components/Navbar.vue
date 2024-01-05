<template>
  <div>
    <header id="header" class="header">
      <div class="container">
        <div class="row">
          <div class="four columns pb-4">
            <img src="../img/logo.gif" id="logo" />
          </div>
          <div class="two columns u-pull-right">
            <ul>
              <li class="submenu">
                <img class="pt-4" src="../img/cart.png" id="img-carrito" />
                <div id="carrito">
                  <table id="lista-carrito" class="u-full-width">
                    <thead>
                      <tr>
                        <th>Imagen</th>
                        <th>Nombre</th>
                        <th>Precio</th>
                        <th>Cantidad</th>
                        <th></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="item in articulosCarritos" :key="item.id">
                        <td><img :src="item.imagen" width="100" /></td>
                        <td>{{ item.nombre }}</td>
                        <td>{{ item.precio }}</td>
                        <td>{{ item.cantidad }}</td>
                        <td>
                          <a
                            href="#"
                            class="borrar-curso"
                            @click="eliminarCurso(item.id)"
                            >X</a
                          >
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <a
                    href="#"
                    id="vaciar-carrito"
                    class="button u-full-width"
                    @click="vaciarCarrito"
                    >Vaciar Carrito</a
                  >
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  props: {
    articulosCarritos: {
      type: Array,
      required: true,
    },
  },
  methods: {
    eliminarCurso(cursoId) {
      this.$emit("eliminar-curso", cursoId); // Emite el evento para eliminar el curso
    },
    vaciarCarrito() {
      this.$emit("vaciar-carrito"); // Emite el evento para vaciar el carrito
    },
  },
};
</script>

<style>
/* Estilos opcionales para este componente */
</style>
