<template lang="">
  <header id="header" class="header">
    <div class="container">
      <div class="row">
        <div class="four columns">
          <img src="../assets/img/nazaret-logo.gif" id="logo" />
        </div>
        <div class="two columns u-pull-right">
          <ul>
            <li class="submenu">
              <img src="../assets/img/cart.png" id="img-carrito" />
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
                  <tbody></tbody>
                </table>

                <a href="#" id="vaciar-carrito" class="button u-full-width"
                  >Vaciar Carrito</a
                >
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>
<script>
export default {};
</script>
<style lang=""></style>
