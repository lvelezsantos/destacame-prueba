<template>
  <div>
    <div class="row">
      <div class="col-6">
        <b-form @submit="onSubmit" v-if="show">
          <b-form-group id="input-group-name" label="Nombre:" label-for="input-name">
            <b-form-input
                id="input-name"
                v-model="form.name"
                placeholder="Ingrese el nombre del lugar"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-description" label="Descripcion:" label-for="input-description">
            <b-form-textarea
                id="input-description"
                v-model="form.description"
                placeholder="Ingrese la descripcion"
                required
            ></b-form-textarea>
          </b-form-group>

          <b-button class="mr-2" type="submit" variant="primary">Enviar</b-button>
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
  created() {
    this.find();

  },
  data() {
    return {
      form: {
        name: '',
        description: '',
      },
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/places/' + this.$route.params.id + '/'
      let place_name = this.form.name
      axios.put(url, {
        name: place_name,
        description: this.form.description,
      })
      .then(function (response) {
        alert('el lugar "' + place_name + '" ha sido actualizado')
        router.push({name: 'place-list'})
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
        alert(JSON.stringify(error.response));
      });
      // alert(JSON.stringify(this.form))
    },

    find: function () {
      let url = config.API_LOCATION + '/api/places/' + this.$route.params.id
      let _this = this;
      axios.get(url)
          .then(function (res){
              _this.form.name = res.data.name;
              _this.form.description = res.data.description;
          });

    },
  }
}
</script>