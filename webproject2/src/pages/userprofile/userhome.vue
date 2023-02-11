<template>
    <div>
        <el-col :span="5" :offset="2" style="background: yellow; margin-top:2%">
            <h1>part 1</h1>
            <div style="margin-left:15%" class="demo-type">
                <div>
                <el-avatar :size="200" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                <el-button class="el-icon-edit"></el-button>
                </div>
            </div>
            
        </el-col>
        <el-col :span="10" :offset="2" style="background: gray;  margin-top:2%">
            <h1> part 2</h1>
            <el-row  :span="5" :offset="2" style="background: #1F3D70; border-radius: 50px;width: 200px;">
                <span style="margin-left:27%;font-family: 'Inter'; font-style: normal; font-weight: 400; font-size: 30px; line-height: 61px; color: #F5EFE0;">Profile</span>
            </el-row>


        </el-col>

    </div>

</template>

<script>
export default {
    data() {
      return {
      }
    }
  }

</script>

<style >

</style>
