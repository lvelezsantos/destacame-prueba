<template>
  <div>
    <div class="row">
      <div class="col-6">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group id="input-group-name" label="Nombre:" label-for="input-name">
            <b-form-input
                id="input-name"
                v-model="form.name"
                placeholder="Ingrese el nombre del lugar"
                required
            ></b-form-input>
          </b-form-group>

          <b-button class="mr-2" type="submit" variant="primary">Submit</b-button>
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
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/places/'
      let place_name = this.form.name
      axios.post(url, {
        name: place_name,
      })
      .then(function (response) {
        alert('el lugar "' + place_name + '" ha sido creado')
        router.push({name: 'place-list'})
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