<template>
  <div>
    <div class="row">
      <div class="col-6">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group id="input-group-name" label="Nombre:" label-for="input-name">
            <b-form-input
                id="input-name"
                v-model="form.name"
                placeholder="Ingrese el nombre del pasajero"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-identification" label="Identificacion:" label-for="input-identification">
            <b-form-input
                id="input-identification"
                v-model="form.identification"
                placeholder="Ingrese la identificacion del pasajero"
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
        identification: '',
      },
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/passengers/'
      let form = this.form
      axios.post(url, {
        name: form.name,
        identification: form.identification,
      })
      .then(function (response) {
        alert('el pasajero "' + form.name + '" ha sido creado')
        router.push({name: 'passenger-list'})
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
      this.form.identification = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>