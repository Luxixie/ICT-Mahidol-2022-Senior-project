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
        path:'/sendemail',
        component:()=>import('../pages/login/sendemailpage.vue')
      },
      {
          path:'/newpassword',
          component:()=>import('../pages/login/newpasswordPage.vue')
      },
      {
        path:'/completeresetpassword',
        component:()=>import('../pages/login/completeresetpassword.vue')
      },
      {
        path:'/home2',
        component:()=>import('../pages/home/homePage2.vue')
      },
      {
        path:'/opentest',
        component:()=>import('../pages/knowledge/opentest.vue')
      },
      {
        path:'/test',
        component:()=>import('../pages/knowledge/test.vue')
      },
      {
        path:'/markethome',
        component:()=>import('../pages/marketinform/markethome.vue')
      },


    ]

})

export default  router