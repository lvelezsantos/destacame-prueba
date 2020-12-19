<template>

  <div class="container">
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <h3>{{ element.name }}</h3>
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
          text: 'Conductores',
          to: {name: 'driver-list'}
        },
        {
          text: 'Detalle del Conductor',
          active: true
        }
      ]
    }
  },
  methods: {
    find: function () {
      let url = config.API_LOCATION + '/api/drivers/' + this.$route.params.id
      axios.get(url)
          .then(res => this.element = res.data)

    },
  }
}
</script>

<style>
</style>