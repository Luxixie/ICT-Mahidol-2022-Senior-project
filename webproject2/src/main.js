import Vue from 'vue'
import App from './App.vue'
import router from './router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'
import mockdata from "./mock/mock";
import store from './store';
import * as echarts from 'echarts';
import locale from 'element-ui/lib/locale/lang/en'

Vue.use(ElementUI, { locale })


Vue.prototype.$echarts = echarts;
Vue.config.productionTip = false
Vue.use(ElementUI)

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')

const cors = require('cors');
const corsOptions ={
    origin:'http://localhost:8080', 
    credentials:true,            //access-control-allow-credentials:true
    optionSuccessStatus:200
}
app.use(cors(corsOptions));