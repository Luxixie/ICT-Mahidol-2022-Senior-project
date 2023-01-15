import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);


const router = new Router({
    mode: "history",
    routes:[
      {path:"/",redirect:'/home'},
      {
        path:'/home',
        component:()=>import('../pages/home/homePage.vue')
      },
      {
        path:'/login',
        component:()=>import('../pages/login/loginPage.vue')
      },
      {
        path:'/signup',
        component:()=>import('../pages/login/signupPage.vue')
      } ,
      {
          path:'/forgetpassword',
          component:()=>import('../pages/login/forgetpasswordPage.vue')
      }
      ,
      {
          path:'/newpassword',
          component:()=>import('../pages/login/newpasswordPage.vue')
      }

    ]

})

export default  router