<template>

  <div class="container">
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <h3>{{ element.name }}</h3>
    <p v-if="element.description">
      {{ element.description }}
    </p>
    <p v-else>-</p>
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
          text: 'Lugares',
          to: {name: 'place-list'}
        },
        {
          text: 'Detalle del lugar',
          active: true
        }
      ]
    }
  },
  methods: {
    find: function () {
      let url = config.API_LOCATION + '/api/places/' + this.$route.params.id
      axios.get(url)
          .then(res => this.element = res.data)

    },
  }
}
</script>

<style>
</style>