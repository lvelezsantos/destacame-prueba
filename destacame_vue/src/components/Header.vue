<template>
  <div>
      <b-navbar variant="dark" type="dark">
            <b-navbar-brand to="/">Destacame</b-navbar-brand>
          <b-navbar-nav class="">
            <b-nav-item :to="{ name: 'passenger-list' }">Pasajeros</b-nav-item>
            <b-nav-item :to="{ name: 'route-list' }">Rutas</b-nav-item>
            <b-nav-item :to="{ name: 'schedule-list' }">Programacion de Rutas</b-nav-item>
            <b-nav-item-dropdown text="Configuracion" right>
              <b-dropdown-item :to="{ name:'place-list' }">Lugares</b-dropdown-item>
              <b-dropdown-item :to="{ name:'driver-list' }">Conductores</b-dropdown-item>
              <b-dropdown-item :to="{ name:'bus-list' }">Buses</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>

        </b-navbar>
  </div>
</template>

<script>
export default {
    created() {
        // this.findAll();
    },
    data(){
        return {
        }
    },
    methods: {
        
    }
}
</script>

<style>
</style>