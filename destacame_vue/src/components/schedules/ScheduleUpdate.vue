<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>
    <div class="row">
      <div class="col-12">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">


          <b-form-group id="input-group-start" label="Salida:" label-for="input-start">
            <div class="row">
              <div class="col-6">
                <b-form-datepicker id="datepicker-start" v-model="form.start.date" class="mb-2"></b-form-datepicker>
              </div>
              <div class="col-6">
                <b-form-timepicker v-model="form.start.time" locale="en"></b-form-timepicker>
              </div>
            </div>
          </b-form-group>
          <b-form-group id="input-group-name" label="Llegada:" label-for="input-name">
            <div class="row">
              <div class="col-6">
                <b-form-datepicker id="datepicker-end" v-model="form.end.date" class="mb-2"></b-form-datepicker>

              </div>
              <div class="col-6">
                <b-form-timepicker v-model="form.end.time" locale="en"></b-form-timepicker>
              </div>
            </div>

          </b-form-group>
          <b-form-group id="input-group-bus" label="Bus:" label-for="select-destination">
                <b-form-select v-model="form.bus" :options="buses" text-field="name" value-field="id"></b-form-select>
          </b-form-group>

          <b-form-group id="input-group-routes" label="Ruta:" label-for="select-destination">
            <b-form-select v-model="form.route" :options="routes" text-field="repr" value-field="id"></b-form-select>
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
import moment from "moment";

const axios = require('axios');


export default {
  data() {
    return {
      buses: [],
      routes: [],
      form: {
        start: {date: '', time: ''},
        end: {date: '', time: ''},
        bus: '',
        route: '',
      },
      show: true,
      breadcrumb_items: [
        {
          text: 'Inicio',
          to: {name: 'home'}
        },
        {
          text: 'Programacion de Rutas',
          to: {name: 'schedule-list'}
        },
        {
          text: 'Programar Ruta',
          active: true
        }
      ],
    }
  },
  created() {
    this.findSchedule()
    this.findBus()
    this.findRoutes()
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      let router = this.$router;
      let url = config.API_LOCATION + '/api/schedules/' + this.$route.params.id + '/'
      let form = this.form

      axios.put(url, {
        start: form.start.date + 'T' + form.start.time,
        end: form.end.date + 'T' + form.end.time,
        bus: form.bus,
        route: form.route,
      })
          .then(function (response) {
            alert('Se ha actualizado la programacion de la ruta correctamente')
            router.push({name: 'schedule-list'})
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            alert(JSON.stringify(error.response));
          });
      // alert(JSON.stringify(this.form))
    },
    findBus() {
      var url = config.API_LOCATION + '/api/buses/'
      axios.get(url)
          .then(res => this.buses = res.data)
    },
    findRoutes() {
      var url = config.API_LOCATION + '/api/routes/'
      axios.get(url)
          .then(res => this.routes = res.data)
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form = {
        start: {date: '', time: ''},
        end: {date: '', time: ''},
        bus: '',
        route: '',
      }
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    findSchedule: function () {
      let _this = this;
      let url = config.API_LOCATION + '/api/schedules/' + this.$route.params.id
      axios.get(url)
          .then(res => {
            let data = res.data
            let start = moment(String(data.start))
            data['start'] = {
              date: start.format('YYYY-MM-DD'),
              time: start.format('HH:mm:ss')
            }
            console.log(data)
            let end = moment(String(data.end))
            data['end'] = {
              date: end.format('YYYY-MM-DD'),
              time: end.format('HH:mm:ss')
            }
            _this.form = data
          })

    },
  }
}
</script>