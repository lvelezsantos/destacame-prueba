<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>
    <div class="row">
      <div class="col-6">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group id="input-group-name" label="Nombre:" label-for="input-name">
            <b-form-input
                id="input-name"
                v-model="form.name"
                placeholder="Ingrese el nombre del conductor"
                required
            ></b-form-input>
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
      form: {
        name: '',
      },
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
          text: 'Crear conductor',
          active: true
        }
      ],
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/drivers/'
      let form = this.form
      axios.post(url, {
        name: form.name,
        identification: form.identification,
      })
      .then(function (response) {
        alert('el conductor "' + form.name + '" ha sido creado')
        router.push({name: 'driver-list'})
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
        alert(JSON.stringify(error.response));
      });
      // alert(JSON.stringify(this.form))
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.name = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>