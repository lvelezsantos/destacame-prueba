<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <div class="row mb-3">
      <div class="col-md-6 text-left"><h2>Conductores</h2></div>
      <div class="col-md-6 text-right">
        <router-link class="btn btn-primary pull-right" :to="{name: 'driver-create'}">Añadir</router-link>
      </div>

    </div>

    <b-table striped hover :items="elements" :fields="fields">
      <template #cell(actions)="row">
        <b-button size="sm" :to="{ 'name': 'driver-detail', params: {'id': row.item.id} }" class="mr-1 btn btn-info">
          Ver
        </b-button>
        <b-button size="sm" :to="{ 'name': 'driver-update', params: {'id': row.item.id} }" class="mr-1 btn btn-primary">
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
  name: "DriverList",
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
          text: 'Conductores',
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
        {key: 'name', sortable: false, label: 'Nombre'},
        {key: 'actions', label: 'Acciones', }
      ]
    }
  },
  methods: {
    findAll: function () {
      var url = config.API_LOCATION + '/api/drivers/'
      axios.get(url)
          .then(res => this.elements = res.data)
    },
    hideModal() {
      this.$refs['delete-modal'].hide()
    },
    deleteModal(item, index, button) {
      this.infoModal.title = 'Esta seguro que desea eliminar el conductor: ' + item.name
      this.$root.$emit('bv::show::modal', this.infoModal.id, button)
      this.selectedItem = item
    },
    resetInfoModal() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    deletePlace() {
      let _this = this
      let selectedItem = _this.selectedItem
      var url = config.API_LOCATION + '/api/drivers/' + selectedItem.id
      axios.delete(url)
          .then(res => {
            console.log(res);
            alert('Se ha eliminado el pasajero ' + selectedItem.name)

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
      this.deletePlace()
    },
  }
}
</script>

<style scoped>

</style>