<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <div class="row mb-3">
      <div class="col-md-6 text-left"><h2>Programacion de Rutas</h2></div>
      <div class="col-md-6 text-right">
        <router-link class="btn btn-primary pull-right" :to="{name: 'schedule-create'}">Añadir</router-link>
      </div>

    </div>
    <div class="row mb-3">
      <div class="col-md-12">
        <b-form inline @submit="onSubmit">
          <label class="mr-sm-2">Ocupacion</label>
          <b-form-input
              id="input-name"
              class="mb-2 mr-sm-2 mb-sm-0"
              v-model="form.occupation"
              placeholder="Porcentaje ocupacion"
          ></b-form-input>
          <label class="mr-sm-2">Buses</label>
          <b-form-select
              class="mb-2 mr-sm-2 mb-sm-0"
              v-model="form.bus" :options="buses" text-field="name" value-field="id" :value="null"
          ></b-form-select>

          <b-button type="submit" variant="primary">Filtrar</b-button>
        </b-form>
      </div>
    </div>

    <b-table striped hover :items="elements" :fields="fields">
      <template #cell(start)="data">
        {{ data.item.start|formatDate }}
      </template>
      <template #cell(end)="data">
        {{ data.item.end|formatDate }}
      </template>
      <template #cell(occupation)="data">
        {{ data.item.occupation }} %
      </template>
      <template #cell(actions)="row">
        <b-button size="sm" :to="{ 'name': 'schedule-detail', params: {'id': row.item.id} }" class="mr-1 btn btn-primary">
          Ver Pasajeros
        </b-button>

        <b-button size="sm" :to="{ 'name': 'schedule-update', params: {'id': row.item.id} }" class="mr-1 btn btn-info">
          Editar
        </b-button>

      </template>
    </b-table>

    <b-modal ref="delete-modal" :id="infoModal.id" :title="infoModal.title" @ok="handleOk" @hide="resetInfoModal">
      <pre>{{ infoModal.content }}</pre>
    </b-modal>
  </div>
</template>

<script>

import config from "../../config"

const axios = require('axios');

export default {
  created() {
    this.findAll();
    this.findBus()
  },
  data() {
    return {
      breadcrumb_items: [
        {
          text: 'Inicio',
          to: {name: 'home'}
        },
        {
          text: 'Programacion de Rutas',
          active: true
        }

      ],
      form: {
        occupation: 0,
        bus: null,
      },
      buses: [{name: 'Choose...', id: null}],
      elements: [],
      infoModal: {
        title: '',
        id: 'delete-modal',
        description: '',
      },
      selectedItem: Object,

      fields: [
        {key: 'id', sortable: false},
        {key: 'start', sortable: false, label: 'Salida'},
        {key: 'end', sortable: false, label: 'Llegada'},
        {key: 'bus_data.name', sortable: false, label: 'Bus'},
        {key: 'bus_data.driver_info.name', sortable: false, label: 'Conductor'},
        {key: 'route_data.source_data.name', sortable: false, label: 'Origen'},
        {key: 'route_data.destination_data.name', sortable: false, label: 'Destino'},
        {key: 'occupation', sortable: false, label: 'Ocupacion %'},
        {key: 'passengers_count', sortable: false, label: 'Pasajeros'},
        {key: 'actions', label: 'Acciones',}
      ]
    }
  },
  methods: {
    findAll: function () {
      var url = config.API_LOCATION + '/api/schedules/'
      axios.get(url, {
        params: {
          occupation: this.form.occupation,
          bus: this.form.bus,
        }
      })
          .then(res => this.elements = res.data)
    },
    hideModal() {
      this.$refs['delete-modal'].hide()
    },
    deleteModal(item, index, button) {
      this.infoModal.title = 'Esta seguro que desea eliminar el pasajero: ' + item.name
      this.infoModal.content = item.identification
      this.$root.$emit('bv::show::modal', this.infoModal.id, button)
      this.selectedItem = item
    },
    resetInfoModal() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    findBus() {
      var url = config.API_LOCATION + '/api/buses/'
      axios.get(url)
          .then(res => {
            this.buses = [{name: 'Choose...', id: null}].concat(res.data)

          })
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault()
      // Trigger submit handler
      this.deleteRoute()
    },

    onSubmit(event) {
      event.preventDefault();
      this.findAll()
    }
  }
}
</script>

<style scoped>

</style>