<template>
  <div>
    <div id="hero">
      <div class="container">
        <div class="row">
          <div class="six columns">
            <div class="contenido-hero">
              <h2>Aprende algo nuevo</h2>
              <p>Todos los cursos a 15€</p>
              <form action="#" id="busqueda" method="post" class="formulario">
                <input
                  class="u-full-width"
                  type="text"
                  placeholder="¿Qué te gustaría Aprender?"
                  id="buscador"
                />
                <input
                  type="submit"
                  id="submit-buscador"
                  class="submit-buscador"
                />
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Barra de características -->
    <div class="barra">
      <div class="container">
        <div class="row">
          <div class="four columns icono icono1">
            <p>
              20,000 Cursos en línea <br />
              Explora los temas más recientes
            </p>
          </div>
          <div class="four columns icono icono2">
            <p>
              Instructores Expertos <br />
              Aprende con distintos estilos
            </p>
          </div>
          <div class="four columns icono icono3">
            <p>
              Acceso de por vida <br />
              Aprende a tu ritmo
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // Puedes agregar lógica específica para esta sección si es necesaria
};
</script>

<style scoped>
/* Estilos opcionales para la sección Principal */
</style>
