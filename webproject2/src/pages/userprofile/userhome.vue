<template>
    <div>
        <el-col :span="5" :offset="2" style="background: yellow; margin-top:2%;">
            <h1>part 1</h1>
            <el-row>
                <div style="margin-left:20%">
                    <el-avatar :size="150" :src="avatar"   />
                </div>
                <el-popover
                    placement="top"
                    width="160"
                    trigger="click"
                    v-slot="{reference,popover}" >
                <el-button 
                    size="mini"
                    type="text"
                    class="avatar-modification"
                    ref="reference" 
                    >
                    <i class="el-icon-edit"></i>
                </el-button>
                <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                >
                    <el-button size="small" type="primary">Change Avatar</el-button>
                </el-upload>
                <template v-slot:popover>
                    <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                    >
                    <el-button size="small" type="primary">Change Avatar</el-button>
                    </el-upload>
                </template>
                </el-popover>

            </el-row>

            
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
import { Avatar, Popover, Upload, Button, Icon } from "element-ui";


export default {
  components: {
    ElAvatar: Avatar,
    ElPopover: Popover,
    ElUpload: Upload,
    ElButton: Button,
    ElIcon: Icon
  },
  data() {
    return {
      avatar: "https://avatars0.githubusercontent.com/u/8186664?s=460&v=4",
      visible: false,
    };
  },
    methods: {
    handleAvatarSuccess(response, file, fileList) {
      this.avatar = URL.createObjectURL(file.raw);
    }
  }
};
</script>

<style >

.avatar-modification {
  position: absolute;
  top: -5px;
  right: -5px;
}
</style>
