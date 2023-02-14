<template>
  <div>
    <el-row style="background: gray; margin-top:2%">
      <h1>part1</h1>
      <el-col :span="12" :offset="3" style="background: blue">
        <h2>content</h2>

      </el-col>
    </el-row>
    <el-row style="background: yellow; margin-top:2%">
        <h1>part2</h1>
        <el-row :gutter="20">
          <el-col :span="6">
            <div></div>
            </el-col>
          <el-col :span="6"
          ><div class="grid-content bg-purple"></div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple"></div>
            </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple"></div>
            </el-col>
        </el-row>
    </el-row>
  </div>
  
</template>

<script>

</script>


<style >
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }

</style>