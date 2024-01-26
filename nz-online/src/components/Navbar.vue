<template>
  <div>
    <header id="header" class="header">
      <div class="container">
        <div class="row">
          <div class="four columns pb-3">
            <img src="../img/logo.svg" id="logo" />
          </div>
          <div class="two columns u-pull-right">
            <ul>
              <li class="submenu">
                <img class="pt-6" src="../img/cart.svg" id="img-carrito" />
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
.header {
  padding: 20px 0;
  background: #8fd3f4; /* Azul claro */
  background: -moz-linear-gradient(left, #8fd3f4 0%, #85e3a6 100%);
  background: -webkit-linear-gradient(left, #8fd3f4 0%, #85e3a6 100%);
  background: linear-gradient(to right, #8fd3f4 0%, #85e3a6 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#8fd3f4', endColorstr='#85e3a6', GradientType=1);
}</style>
