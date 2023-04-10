<template>
  <div id="newpassword-div">
    <el-row>
      <el-col id="newpassword-title-col" :span="24" :offset="10">
        <h1 id="newpassword-title">Reset Password</h1>
      </el-col>
    </el-row>
    <el-row>
      <el-col id="newpassword-title-info" :span="24" :offset="9">
        <span>Choose a new password for your account.</span>
      </el-col>
    </el-row>
    <el-form id="newpassword-form" ref="form" :model="form">
      <el-form-item
        label="Password"
        style="font-weight: bold; color: aliceblue"
      >
        <el-input
          id="newpassword-input"
          placeholder="Password"
          show-password
          v-model="form.password"
        ></el-input>
      </el-form-item>
      <el-form-item
        label="Confirm Password"
        style="font-weight: bold; color: aliceblue"
      >
        <el-input
          id="newpassword-input"
          placeholder="Confirm Password"
          show-password
          v-model="form.confirmPassword"
        />
      </el-form-item>
      <el-form-item>
        <el-button
          round
          type="warning"
          @click="submitForm()"
          style="width: 45%; margin-left: 25%; float: left"
          >submit</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import  axios from "axios"
export default {
  data() {
    return {
      form: {
        email: "",
        password: "",
        confirmPassword: "",
      },
    };
  },
  created() {
    console.log(this.$store.state.email);
    this.form.email = this.$store.state.email
  },
  methods: {
    validatePassword() {
      if (this.form.password === this.form.confirmPassword) {
        console.log(this.form.password);
        console.log(this.form.confirmPassword);
        if (this.form.password.length < 8) {
          //console.log("Passwords do not longer than 8");
          this.$alert('Passwords do not longer than 8', 'Password error', {
          confirmButtonText: 'Next',
            })
          return false;
        }

        // check number
        if (!/\d/.test(this.form.password)) {
          //console.log("Passwords do not include number");
          this.$alert('Passwords do not include number', 'Password error', {
          confirmButtonText: 'Next',
            })
          return false;
        }

        // check the symbol
        if (!/[!@#$%^&*(),.?":{}|<>]/g.test(this.form.password)) {
          //console.log("Passwords do not include symbol");
          this.$alert('Passwords do not include symbol', 'Password error', {
          confirmButtonText: 'Next',
            })
          return false;
        }

        // Check whether it contains at least one uppercase letter and one lowercase letter
        if (
          !/[a-z]/g.test(this.password) ||
          !/[A-Z]/g.test(this.form.password)
        ) {
        this.$alert('Passwords do not include at least one uppercase letter and one lowercase letter', 'Password error', {
          confirmButtonText: 'Next',
        })
          return false;
        }

        // If all conditions are met, the password meets the requirements
        return true;
      } else {
        //console.log();
        //alert("Passwords do not match")
        this.$alert('Passwords do not match', 'Password error', {
          confirmButtonText: 'Next',
      })
      }
    },
    submitForm() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          var checkResult = this.validatePassword();
          if (checkResult) {
            this.Editpassword();
            this.$router.replace("/completeresetpassword");
          }
        } else {
          this.$message({
            showClose: true,
            message: "Form is invalid",
            type: "warning",
          });
        }
      });
    },
    Editpassword() {
      axios
        .post("http://127.0.0.1:8088/editpassword", this.form)
        .then((res) => {
          console.log(res.data);
          if (res.data.state == 1) {
            this.$message({
              showClose: true,
              message: "Successfully modified information",
              type: "success",
            });
          } else {
            alert("Incorrect information");
            return false;
          }
        });
    },
  },
};
</script>

<style>
.newpassword-bt {
  margin-left: 30px;
}
#newpassword-input {
  background: #1f3d70;
  border-color: #1f3d70;
  border-radius: 100px;
  color: #f5efe0;
}

#newpassword-form {
  margin-left: 38%;
  margin-right: 38%;
}

#newpassword-div {
  margin-top: 8%;
}

#newpassword-title {
  color: #f5efe0;
  font-size: 30px;
}

#newpassword-title-info {
  margin-bottom: 3%;
  color: #f5efe0;
}
</style>