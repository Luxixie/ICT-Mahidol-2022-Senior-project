import Vue from "vue";
import Vuex from "vuex"
Vue.use(Vuex)

export default new Vuex.Store({
    state: {
      token: '',
      username: ''
    },
    getters: {
    },
    mutations: {
      SET_TOKEN(state, token){
        state.token = token ;
        localStorage.setItem("token",token);
      },
      SET_UserName(state, username){
        state.username = username ;
        console.log(username)
        localStorage.setItem("username",username);
      },
      resetState(state){
        state.token = '';
        localStorage.clear();
    }
    },
    actions: {
    },
    modules: {
    }
  })
  