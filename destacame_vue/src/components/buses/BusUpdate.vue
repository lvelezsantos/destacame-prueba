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
                placeholder="Ingrese el nombre del bus"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-driver" label="Conductor:" label-for="select-destination">
            <b-form-select v-model="form.driver" :options="drivers" text-field="name" value-field="id"></b-form-select>
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
      drivers: [],
      form: {
        name: '',
        driver: '',
      },
      show: true,
      breadcrumb_items: [
        {
          text: 'Inicio',
          to: {name: 'home'}
        },
        {
          text: 'Buses',
          to: {name: 'bus-list'}
        },
        {
          text: 'Actualizar Bus',
          active: true
        }
      ],
    }
  },
  created() {
    this.findDrivers()
    this.find()
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/buses/' + this.$route.params.id + '/'
      let form = this.form

      axios.put(url, {
        name: form.name,
        driver: form.driver,
      })
          .then(function (response) {
            alert('el bus ha sido actualizado')
            router.push({name: 'bus-list'})
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            alert(JSON.stringify(error.response));
          });
      // alert(JSON.stringify(this.form))
    },
    findDrivers() {
      var url = config.API_LOCATION + '/api/drivers/'
      axios.get(url)
          .then(res => this.drivers = res.data)
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
    },
    find: function () {
      let url = config.API_LOCATION + '/api/buses/' + this.$route.params.id
      axios.get(url)
          .then(res => this.form = res.data)

    },
  }
}
</script>