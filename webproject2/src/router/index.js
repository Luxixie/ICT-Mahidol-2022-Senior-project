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
        path: '/wishlist',
        component: () => import('../pages/stock/wishlistPage.vue')
      },
      {
        path:'/opentest',
        component:()=>import('../pages/knowledge/opentest.vue')
      },
      {
        path:'/test',
        component:()=>import('../pages/test/test.vue')
      },
      {
        path:'/markethome',
        component:()=>import('../pages/marketinform/markethome.vue')
      },

      {
        path:'/userhome',
        component:()=>import('../pages/userprofile/userhome.vue')
      },

      {
        path:'/stockinformation',
        component:()=>import('../pages/stock/stockInfoPage.vue')
      },
      {
        path:'/knowledgeHome',
        component:()=>import('../pages/knowledge/knowledgeHome.vue')
      },
      {
        path:'/chapter1',
        component:()=>import('../pages/knowledge/Chapters/Chapter1/chapter1Home.vue')
      },
      {
        path:'/chapter2',
        component:()=>import('../pages/knowledge/Chapters/Chapter2/chapter2Home.vue')
      },
      {
        path:'/chapter3',
        component:()=>import('../pages/knowledge/Chapters/Chapter3/chapter3Home.vue')
      },
      {
        path:'/chapter4',
        component:()=>import('../pages/knowledge/Chapters/Chapter4/chapter4Home.vue')
      },
      {
        path:'/chapter5',
        component:()=>import('../pages/knowledge/Chapters/Chapter5/chapter5Home.vue')
      },
      {
        path:'/chapter6',
        component:()=>import('../pages/knowledge/Chapters/Chapter6/chapter6Home.vue')
      },
      {
        path:'/chapter2.1',
        component:()=>import('../pages/knowledge/Chapters/Chapter2/chapter2.1.vue')
      },
      {
        path:'/chapter2test',
        component:()=>import('../pages/knowledge/Chapters/Chapter2/Questions/chapter2test.vue')
      }




    ]

})

export default  router