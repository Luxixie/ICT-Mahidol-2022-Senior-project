<template>
    <div id="test-bt">
        <h1>Opening test 1 of 6</h1>
        <span>Which one of the following is computed by divided by the current stock price?</span>
        <el-row>
            <el-radio-group v-model="radio1">
            <el-radio-button label="A. Yield to maturity"></el-radio-button>
            <el-radio-button label="B. Capital gains yield"></el-radio-button>
            <el-radio-button label="C. Dividend yield"></el-radio-button>
            <el-radio-button label="D. I don’t know"></el-radio-button>
        </el-radio-group>
        </el-row>
    </div>
</template>

<script>
export default {
    data(){
        return {
            radio1:''
        }
    }
}
</script>

<style>

</style>