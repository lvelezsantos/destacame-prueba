<template>

  <div class="container">
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <h3>{{ element.source_data.name }} - {{element.destination_data.name}}</h3>
    <ul>
      <li><strong>Pasajeros: </strong> {{element.passengers}}</li>
      <li><strong>Rutas Programadas: </strong> {{element.schedules_count}}</li>
      <li><strong>Promedio de pasajeros: </strong> {{element.passenger_avg}}</li>
    </ul>
  </div>
</template>

<script>

import config from "../../config"

const axios = require('axios');


export default {
  created() {
    this.find();

  },
  data() {
    return {
      element: Object,
      breadcrumb_items: [
        {
          text: 'Inicio',
          to: {name: 'home'}
        },
        {
          text: 'Rutas',
          to: {name: 'route-list'}
        },
        {
          text: 'Detalle de la ruta',
          active: true
        }
      ]
    }
  },
  methods: {
    find: function () {
      let url = config.API_LOCATION + '/api/routes/' + this.$route.params.id
      axios.get(url)
          .then(res => this.element = res.data)

    },
  }
}
</script>

<style>
</style>