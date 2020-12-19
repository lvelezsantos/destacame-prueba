<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <div class="row mb-3">
      <div class="col-md-6 text-left"><h2>Pasajeros</h2></div>
      <div class="col-md-6 text-right">
        <router-link class="btn btn-primary pull-right" :to="{name: 'passenger-create'}">Añadir</router-link>
      </div>

    </div>

    <b-table striped hover :items="elements" :fields="fields">
      <template #cell(actions)="row">
        <b-button size="sm" :to="{ 'name': 'passenger-detail', params: {'id': row.item.id} }" class="mr-1 btn btn-info">
          Ver
        </b-button>
        <b-button size="sm" :to="{ 'name': 'passenger-update', params: {'id': row.item.id} }" class="mr-1 btn btn-primary">
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
  name: "PassengerList",
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
          text: 'Pasajeros',
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
        {key: 'identification', sortable: false, label: 'Identificacion'},
        {key: 'actions', label: 'Acciones', }
      ]
    }
  },
  methods: {
    findAll: function () {
      var url = config.API_LOCATION + '/api/passengers/'
      axios.get(url)
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
    deletePassenger() {
      let _this = this
      let selectedItem = _this.selectedItem
      var url = config.API_LOCATION + '/api/passengers/' + selectedItem.id
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
      this.deletePassenger()
    },
  }
}
</script>

<style scoped>

</style>