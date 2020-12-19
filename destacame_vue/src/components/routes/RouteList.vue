<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <div class="row mb-3">
      <div class="col-md-6 text-left"><h2>Rutas</h2></div>
      <div class="col-md-6 text-right">
        <router-link class="btn btn-primary pull-right" :to="{name: 'route-create'}">Añadir</router-link>
      </div>

    </div>

    <b-table striped hover :items="elements" :fields="fields">
      <template #cell(actions)="row">
        <b-button size="sm" :to="{ 'name': 'route-detail', params: {'id': row.item.id} }" class="mr-1 btn btn-info">
          Ver
        </b-button>
        <b-button size="sm" :to="{ 'name': 'route-update', params: {'id': row.item.id} }" class="mr-1 btn btn-primary">
          Editar
        </b-button>
        <b-button class="btn btn-danger" size="sm" @click="deleteModal(row.item, row.index, $event.target)">
          Eliminar
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
  },
  data() {
    return {
      msj: '...:(',
      breadcrumb_items: [
        {
          text: 'Inicio',
          to: {name: 'home'}
        },
        {
          text: 'Rutas',
          active: true
        }

      ],
      elements: [],
      infoModal: {
        title: '',
        id: 'delete-modal',
        description: '',
      },
      selectedItem: Object,

      fields: [
        {key: 'id', sortable: false},
        {key: 'source_data.name', sortable: false, label: 'Origin'},
        {key: 'destination_data.name', sortable: false, label: 'Destino'},
        {key: 'passengers', sortable: false, label: 'Pasajeros'},
        {key: 'schedules_count', sortable: false, label: 'Rutas Programadas'},
        {key: 'passenger_avg', sortable: false, label: 'Promedio de pasajeros'},
        {key: 'actions', label: 'Acciones', }
      ]
    }
  },
  methods: {
    findAll: function () {
      var url = config.API_LOCATION + '/api/routes/'
      axios.get(url)
          .then(res => this.elements = res.data)
    },
    hideModal() {
      this.$refs['delete-modal'].hide()
    },
    deleteModal(item, index, button) {
      this.infoModal.title = 'Esta seguro que desea eliminar la ruta: ' + item.repr
      this.$root.$emit('bv::show::modal', this.infoModal.id, button)
      this.selectedItem = item
    },
    resetInfoModal() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    deleteRoute() {
      let _this = this
      let selectedItem = _this.selectedItem
      var url = config.API_LOCATION + '/api/routes/' + selectedItem.id
      axios.delete(url)
          .then(res => {
            console.log(res);
            alert('Se ha eliminado la ruta ' + selectedItem.repr)

            _this.hideModal()
            _this.findAll()
          })
          .catch(function (error) {
            console.log(error)
          })

    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault()
      // Trigger submit handler
      this.deleteRoute()
    },
  }
}
</script>

<style scoped>

</style>