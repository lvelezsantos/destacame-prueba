<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>
    <div class="row">
      <div class="col-6">
        <b-form @submit="onSubmit" v-if="show">
          <b-form-group id="input-group-name" label="Nombre:" label-for="input-name">
            <b-form-input
                id="input-name"
                v-model="form.name"
                placeholder="Ingrese el nombre del conductor"
                required
            ></b-form-input>
          </b-form-group>

          <b-button class="mr-2" type="submit" variant="primary">Enviar</b-button>
        </b-form>
      </div>
    </div>
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
      formFields: ['name'],
      form: {
        name: '',
      },
      show: true,
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
          text: 'Actualizar Conductor',
          active: true
        }
      ],
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/drivers/' + this.$route.params.id + '/'
      let form = this.form
      axios.put(url, {
        name: form.name,
      })
          .then(function (response) {
            alert('el conductor "' + form.name + '" ha sido actualizado')
            router.push({name: 'driver-list'})
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            alert(JSON.stringify(error.response));
          });
      // alert(JSON.stringify(this.form))
    },

    find: function () {
      let url = config.API_LOCATION + '/api/drivers/' + this.$route.params.id
      let _this = this;
      axios.get(url)
          .then(function (res) {
            _this.form.name = res.data.name;
          });

    },
  }
}
</script>