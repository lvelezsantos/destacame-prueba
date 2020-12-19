<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>
    <div class="row">
      <div class="col-6">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group id="input-group-source" label="Origen:" label-for="select-source">
            <b-form-select v-model="form.source" :options="places" text-field="name" value-field="id"
                           label="Origen"></b-form-select>
          </b-form-group>
          <b-form-group id="input-group-destination" label="Destino:" label-for="select-destination">
            <b-form-select v-model="form.destination" :options="places" text-field="name"
                           value-field="id"></b-form-select>
          </b-form-group>


          <b-button class="mr-2" type="submit" variant="primary">Enviar</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </div>
    </div>
    <!--    <b-card class="mt-3" header="Form Data Result">-->
    <!--      <pre class="m-0">{{ form }}</pre>-->
    <!--    </b-card>-->
  </div>
</template>

<script>

import config from "../../config"

const axios = require('axios');


export default {
  data() {
    return {
      places: [],
      form: {
        source: '',
        destination: '',
      },
      show: true,
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
          text: 'Actualizar Ruta',
          active: true
        }
      ],
    }
  },
  created() {
    this.findPlaces()
    this.find()
  },
  methods: {
    find: function () {
      let url = config.API_LOCATION + '/api/routes/' + this.$route.params.id
      axios.get(url)
          .then(res => this.form = res.data)

    },
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/routes/' + this.$route.params.id + '/'
      let form = this.form
      console.log(form);
      axios.put(url, {
        source: form.source,
        destination: form.destination,
      })
          .then(function (response) {
            alert('la ruta ha sido actualizada')
            router.push({name: 'route-list'})
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            alert(JSON.stringify(error.response));
          });
      // alert(JSON.stringify(this.form))
    },
    findPlaces() {
      var url = config.API_LOCATION + '/api/places/'
      axios.get(url)
          .then(res => this.places = res.data)
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.source = ''
      this.form.destination = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>