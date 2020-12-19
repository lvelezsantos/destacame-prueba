<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>
    <div class="row">
      <div class="col-12" v-if="schedule">
        <h3>Ruta {{ schedule.route_data.source_data.name }} ({{ schedule.start|formatDate }}) -
          {{ schedule.route_data.destination_data.name }} ({{ schedule.end|formatDate }})</h3>
        <ul class="mb-3">
          <li><strong>Bus: </strong> {{ schedule.bus_data.name }} ( {{ schedule.bus_data.driver_info.name }} )</li>
          <li><strong>Capacidad del Bus: </strong> {{ schedule.bus_data.capacity }}</li>
          <li><strong>Pasajeros: </strong> {{ schedule.passengers_count }}</li>
          <li><strong>Ocupacion: </strong> {{ schedule.occupation }} %</li>
        </ul>

        <div class="row mb-3">
          <div class="col-md-12">
            <b-form inline @submit="onSubmit">
              <label class="mr-sm-2">Pasajero</label>
              <b-form-select
                  class="mb-2 mr-sm-2 mb-sm-0"
                  v-model="form.passenger" :options="passengers" text-field="name" value-field="id" :value="null"
              ></b-form-select>
              <label class="mr-sm-2">Asiento</label>
              <b-form-select
                  class="mb-2 mr-sm-2 mb-sm-0"
                  v-model="form.seat" :options="seats" text-field="name" value-field="id" :value="null"
              ></b-form-select>

              <b-button type="submit" variant="primary">Asignar Asiento</b-button>
            </b-form>
          </div>
        </div>

        <b-table striped hover :items="schedule.passengers_list" :fields="fields">
<!--          <template #cell(actions)="row">-->
<!--            <b-button size="sm" :to="{ 'name': 'schedule-detail', params: {'id': row.item.id} }"-->
<!--                      class="mr-1 btn btn-info">-->
<!--              Ver-->
<!--            </b-button>-->

<!--          </template>-->
        </b-table>
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
      // buses: [],
      // routes: [],
      schedule: null,
      show: true,
      passengers: [],
      seats: [],
      form: {
        passenger: null,
        seat: null
      },
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
          text: 'Detalle de Ruta',
          active: true
        }
      ],
      fields: [
        {key: 'id', sortable: false},
        {key: 'passenger_data.name', sortable: false, label: 'Pasajero'},
        {key: 'passenger_data.identification', sortable: false, label: 'Identificacion'},
        {key: 'seat', sortable: false, label: 'Silla'},
        {key: 'actions', label: 'Acciones',}
      ]
    }
  },
  created() {
    this.findSchedule()
    this.findPassengers()
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      // let router = this.$router;
      let url = config.API_LOCATION + '/api/passenger-schedules/'
      let form = this.form
      let _this = this;
      console.log(form);
      axios.post(url, {
        schedule: _this.schedule.id,
        passenger: form.passenger,
        seat: form.seat,
      })
          .then(function (response) {
            alert('Se ha asignado la silla correctamente')
            // _this.schedule = null
            _this.schedule.passengers_list = []
            _this.findSchedule()
            // router.push({name: 'schedule-list'})
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            alert(JSON.stringify(error.response));
          });
      // alert(JSON.stringify(this.form))
    },
    findSchedule: function () {
      let _this = this;
      let url = config.API_LOCATION + '/api/schedules/' + this.$route.params.id
      axios.get(url)
          .then(res => {
            _this.schedule = res.data
            _this.generateSeats()
          })

    },
    findPassengers() {
      var url = config.API_LOCATION + '/api/passengers/'
      axios.get(url)
          .then(res => {
            this.passengers = [{name: 'Choose...', id: null}].concat(res.data)

          })
    },
    generateSeats() {


      let used_seats = []
      this.schedule.passengers_list.forEach(function (value) {
        used_seats.push(value.seat)
      });

      this.seats = [{name: 'Choose...', id: null}]
      for (let i=1; i <= this.schedule.bus_data.capacity; i++) {
        if(used_seats.indexOf(i) == -1) {
          this.seats.push({
            name: i, id: i
          });
        }
      }

      console.log(used_seats)
      console.log(this.seats)
    },
  }
}
</script>