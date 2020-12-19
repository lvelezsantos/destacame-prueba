<template>
  <div>
    <b-breadcrumb :items="breadcrumb_items"></b-breadcrumb>

    <div class="row mb-3">
      <div class="col-md-6 text-left"><h2>Buses</h2></div>
      <div class="col-md-6 text-right">
        <router-link class="btn btn-primary pull-right" :to="{name: 'bus-create'}">Añadir</router-link>
      </div>

    </div>

    <b-table striped hover :items="elements" :fields="fields">
      <template #cell(actions)="row">
        <b-button size="sm" :to="{ 'name': 'bus-detail', params: {'id': row.item.id} }" class="mr-1 btn btn-info">
          Ver
        </b-button>
        <b-button size="sm" :to="{ 'name': 'bus-update', params: {'id': row.item.id} }" class="mr-1 btn btn-primary">
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
      breadcrumb_items: [
        {
          text: 'Inicio',
          to: {name: 'home'}
        },
        {
          text: 'Buses',
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
        {key: 'driver_info.name', sortable: false, label: 'Conductor'},
        {key: 'actions', label: 'Acciones', }
      ]
    }
  },
  methods: {
    findAll: function () {
      var url = config.API_LOCATION + '/api/buses/'
      axios.get(url)
          .then(res => this.elements = res.data)
    },
    hideModal() {
      this.$refs['delete-modal'].hide()
    },
    deleteModal(item, index, button) {
      this.infoModal.title = 'Esta seguro que desea eliminar el bus: ' + item.name
      this.infoModal.content = item.identification
      this.$root.$emit('bv::show::modal', this.infoModal.id, button)
      this.selectedItem = item
    },
    resetInfoModal() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    deleteBus() {
      let _this = this
      let selectedItem = _this.selectedItem
      var url = config.API_LOCATION + '/api/buses/' + selectedItem.id
      axios.delete(url)
          .then(res => {
            console.log(res);
            alert('Se ha eliminado el bus ' + selectedItem.name)

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
      this.deleteBus()
    },
  }
}
</script>

<style scoped>

</style>