import Vue from "vue";
import Vuex from "vuex"
Vue.use(Vuex)

export default new Vuex.Store({
    state: {
      token: '',
      username: '',
      accountid:'',
      region:'',
      birthdate:'',
      email:'',
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
      SET_Accountid(state, accountid){
        state.accountid = accountid ;
        console.log(accountid)
        localStorage.setItem("accountid",accountid);
      },
      SET_Region(state, region){
        state.region = region ;
        console.log(region)
        localStorage.setItem("region",region);
      },
      SET_Birthdate(state, birthdate){
        state.birthdate = birthdate ;
        console.log(birthdate)
        localStorage.setItem("birthdate",birthdate);
      },
      SET_Email(state, email){
        state.email = email ;
        console.log(email)
        localStorage.setItem("email",email);
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
  
  