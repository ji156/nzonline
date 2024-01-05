<template>
  <div>
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
              <h4>{{ curso.nombre }}</h4>
              <p>{{ curso.autor }}</p>
              <img src="../img/estrellas.png" />
              <p class="precio">
                {{ convertirPrecio(curso.precio, curso.pais) }}
                <span class="u-pull-right">{{
                  convertirPrecio(15, curso.pais)
                }}</span>
              </p>
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
      userCountry: "",
      conversionRates: {},
    };
  },
  mounted() {
    this.getUserCountry();
    this.obtenerConversionRates();
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
    getUserCountry() {
      axios
        .get("http://ip-api.com/json")
        .then((response) => {
          this.userCountry = response.data.countryCode;
        })
        .catch((error) => {
          console.error("Error al obtener la ubicación del usuario:", error);
        });
    },
    obtenerConversionRates() {
      const API_KEY = "05a73cfc619105e7ab515fe8";
      const BASE_URL = `https://v6.exchangeratesapi.io/latest?base=USD&access_key=${API_KEY}`;

      axios
        .get(BASE_URL)
        .then((response) => {
          this.conversionRates = response.data.rates;
        })
        .catch((error) => {
          console.error("Error al obtener los tipos de cambio:", error);
        });
    },
    convertirPrecio(precio, pais) {
      const factorConversion = this.conversionRates[pais] || 1;
      const precioConvertido = (precio * factorConversion).toFixed(2);
      return `${this.getMoneda(pais)} ${precioConvertido}`;
    },
    getMoneda(pais) {
      const monedas = {
        US: "$",
        MX: "$",
        EU: "€",
        THA: "฿",
        COL: "$",
        AR: "$",
        PE: "S/",
        CH: "¥",
        BR: "R$",
        VE: "Bs",
        CO: "$",
        CR: "₡",
        EC: "$",
        PA: "B/.",
        PY: "₲",
        UY: "$",
        GT: "Q",
        HN: "L",
        NI: "C$",
        SV: "$",
      };
      return monedas[pais] || "";
    },
    agregarAlCarrito(curso) {
      this.$emit("curso-agregado", curso);
    },
  },
};
</script>

<style>
/* Estilos opcionales para este componente */
</style>
