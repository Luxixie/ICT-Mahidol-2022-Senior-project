<template>
  <el-row class="para1" style="background: #d9d9d9">
    <el-col :span="4">
      <img src="./imges/logo.png" height="100" width="200" />
    </el-col>
    <el-col :span="13">
      <div class="SearchPart">
        <el-input
          id="searchBar"
          placeholder="Search"
          prefix-icon="el-icon-search"
        />
      </div>
    </el-col>
    <el-col :span="5">
      <div class="userInfo" style="margin-top: 10%" v-if="username">
        <el-button size="medium" type="info" round @click="GoHome"
          >Home</el-button
        >
        <el-button style="margin-left: 3%" size="medium" type="info" circle>{{
          username.charAt(0).toUpperCase()
        }}</el-button>
        <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">
            {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item icon="el-icon-user" command="userhome"
              >User profile</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-shopping-cart-2" command="watchlist"
              >Watch list</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-s-finance" command="portfolio"
              >Portfolio</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-tickets" command="quiz"
              >Quiz review</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-refresh-left" command="logout"
              >Log out</el-dropdown-item
            >
          </el-dropdown-menu>
        </el-dropdown>
        <el-badge :value="100" :max="1">
          <el-link icon="el-icon-message-solid" style="width: 5%"></el-link>
        </el-badge>
      </div>

      <div class="LoginPart" v-if="!username" style="margin-top: 8%">
        <el-button size="medium" type="info" round @click="GoLoginPage"
          >Log In</el-button
        >
        <el-button
          id="signupbt"
          size="medium"
          type="info"
          @click="GoSignUpPage"
          round
          >Sign Up</el-button
        >
      </div>
    </el-col>
  </el-row>
</template>
<script>
import { Spinner } from "element-ui";
import { computed } from "vue";
import { mapGetters } from "vuex";

export default {
  name: "Header",
  data() {
    return {};
  },
  methods: {
    GoLoginPage() {
      this.$router.push("/login");
    },
    GoSignUpPage() {
      this.$router.push("/signup");
    },
    GoHome() {
      this.$router.push("/home");
    },
    handleCommand(command) {
      switch (command) {
        case "userhome":
          this.$router.push("/userhome");
          break;
        case "watchlist":
          this.$router.push("/watchlist");
          break;
        case "portfolio":
          this.$router.push("/portfolio");
          break;
        case "quiz":
          this.$router.push("/test");
          break;
        case "logout":
          window.location.href = "/home";
      }
    },
  },
  created() {
    console.log();
  },
  updated() {
    console.log(this.$store.state.username);
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
  },
  watch: {
    "$store.state.username"(newVal, oldVal) {},
  },
  components: { Spinner },
};
</script>

<style>
#signupbt {
  margin-left: 30px;
}

.SearchPart {
  padding: 30px;
  margin-right: 30px;
}

#searchBar {
  background: #f5efe1;
}

.LoginPart {
}

.item {
  margin-top: 10px;
  margin-right: 40px;
}
</style>