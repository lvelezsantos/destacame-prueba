import Vue from 'vue'

import App from './App.vue'

import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
// import VueDynamicForms from '@asigloo/vue-dynamic-forms';

import VueRouter from 'vue-router'

import Home from './components/Home.vue'
import PlaceList from './components/places/PlaceList.vue'
import PlaceDetail from './components/places/PlaceDetail.vue'
import PlaceCreate from './components/places/PlaceCreate.vue'
import PlaceUpdate from './components/places/PlaceUpdate.vue'

import PassengerList from './components/passengers/PassengerList.vue'
import PassengerDetail from './components/passengers/PassengerDetail.vue'
import PassengerCreate from './components/passengers/PassengerCreate.vue'
import PassengerUpdate from './components/passengers/PassengerUpdate.vue'

import DriverList from './components/drivers/DriverList.vue'
import DriverCreate from './components/drivers/DriverCreate.vue'
import DriverDetail from './components/drivers/DriverDetail.vue'
import DriverUpdate from './components/drivers/DriverUpdate.vue'

import RouteList from './components/routes/RouteList.vue'
import RouteCreate from './components/routes/RouteCreate.vue'
import RouteDetail from './components/routes/RouteDetail.vue'
import RouteUpdate from './components/routes/RouteUpdate.vue'

import BusList from './components/buses/BusList.vue'
import BusCreate from './components/buses/BusCreate.vue'
import BusDetail from './components/buses/BusDetail.vue'
import BusUpdate from './components/buses/BusUpdate.vue'

import ScheduleList from './components/schedules/ScheduleList.vue'
import ScheduleCreate from './components/schedules/ScheduleCreate.vue'
import ScheduleDetail from './components/schedules/ScheduleDetail.vue'


// Vue.use(VueDynamicForms);

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VueRouter)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

const routes = [
    {path: "/", component: Home, name: 'home'},
    {path: "/places/create", component: PlaceCreate, name: 'place-create'},
    {path: "/places/:id", component: PlaceDetail, name: 'place-detail'},
    {path: "/places/:id/update", component: PlaceUpdate, name: 'place-update'},
    {path: "/places", component: PlaceList, name: 'place-list'},


    {path: "/passengers", component: PassengerList, name: 'passenger-list'},
    {path: "/passengers/create", component: PassengerCreate, name: 'passenger-create'},
    {path: "/passengers/:id", component: PassengerDetail, name: 'passenger-detail'},
    {path: "/passengers/:id/update", component: PassengerUpdate, name: 'passenger-update'},

    {path: "/drivers", component: DriverList, name: 'driver-list'},
    {path: "/drivers/create", component: DriverCreate, name: 'driver-create'},
    {path: "/drivers/:id", component: DriverDetail, name: 'driver-detail'},
    {path: "/drivers/:id/update", component: DriverUpdate, name: 'driver-update'},

    {path: "/routes", component: RouteList, name: 'route-list'},
    {path: "/routes/create", component: RouteCreate, name: 'route-create'},
    {path: "/routes/:id", component: RouteDetail, name: 'route-detail'},
    {path: "/routes/:id/update", component: RouteUpdate, name: 'route-update'},

    {path: "/buses", component: BusList, name: 'bus-list'},
    {path: "/buses/create", component: BusCreate, name: 'bus-create'},
    {path: "/buses/:id", component: BusDetail, name: 'bus-detail'},
    {path: "/buses/:id/update", component: BusUpdate, name: 'bus-update'},

    {path: "/schedules", component: ScheduleList, name: 'schedule-list'},
    {path: "/schedules/create", component: ScheduleCreate, name: 'schedule-create'},
    {path: "/schedules/:id", component: ScheduleDetail, name: 'schedule-detail'},
]

const router = new VueRouter({
    mode: 'history',
    routes // short for `routes: routes`
})

import moment from 'moment';

Vue.filter('formatDate', function(value) {
    if (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
});

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
