<template>
  <aside :class="{showSidebar:!collapsed}" class="container-aside">
    <div class="menu-toggle" @click.prevent="collapse">
      <i class="icon el-icon-s-fold" v-show="!collapsed" title="Collapse"></i>
      <i class="icon el-icon-s-unfold" v-show="collapsed" title="Expand"></i>
    </div>
    <el-menu router :default-active="$route.path" :collapse="collapsed" ref="leftNavigation">
      <template v-for="(issue, index) in $router.options.routes">
        <template v-if="issue.name === $store.state.leftNavState">
          <template v-for="(item, index) in issue.children">
            <el-submenu v-if="!item.leaf" :index="index+''" v-show="item.menuShow">
              <template slot="title"><i :class="item.iconCls"></i><span slot="title">{{item.name}}</span></template>
              <el-menu-item v-for="link in item.children" :key="link.path" :index="link.path" v-if="link.menuShow"
                            :class="$route.path===link.path?'is-active':''">
                <i :class="item.iconCls"></i><span slot="title">{{item.name}}</span>
              </el-menu-item>
            </el-submenu>
            <el-menu-item v-else-if="item.leaf" :index="item.path"
                          :class="$route.path===item.path?'is-active':''" v-show="item.menuShow">
              <i :class="item.iconCls"></i><span slot="title">{{item.name}}</span>
            </el-menu-item>
          </template>
        </template>
      </template>
    </el-menu>
    <el-button class="help_button">
      <i class="el-icon-info"></i><span v-show="!collapsed">Help assistant</span>
    </el-button>
  </aside>
</template>

<script>
  export default {
    name: "left_nav",
    data() {
      return {
        loading: false,
        collapsed: false
      }
    },
    methods: {
      collapse: function () {
        this.collapsed = !this.collapsed;
      },
      defaultLeftNavOpen() {
        let cur_path = this.$route.path; //get current url path
        let routers = this.$router.options.routes; //get router object
        let subMenuIndex = '';//index for submenu
        let openSubmenu = false; //default for submenu is close
        for (let i = 0; i < routers.length; i++) {
          let children = routers[i].children;
          if (children) {
            for (let j = 0; j < children.length; j++) {
              if (children[j].path === cur_path) {
                break;
              }
              if (children[j].children && !children[j].leaf) {
                let grandChildren = children[j].children;
                for (let z = 0; z < grandChildren.length; z++) {
                  if (grandChildren[z].path === cur_path) {
                    subMenuIndex = j;
                    openSubmenu = true;
                    break;
                  }
                }
              }
            }
          }
        }
        if (this.$refs['leftNavigation'] && openSubmenu) {
          this.$refs['leftNavigation'].open(subMenuIndex);
        }
      }
    },
    watch: {
      '$route': function (to, from) {
        console.log(to.path, from.path);
      }
    },
    mounted() {
      this.defaultLeftNavOpen();
    }
  }
</script>

<style lang="less" scoped>
  .container-aside {
    min-width: 50px;
    background: #333744;

    .menu-toggle {
      background-color: rgba(0, 0, 40, 0.47);
      text-align: center;
      color: white;
      height: 30px;
      line-height: 30px;

      .icon:hover {
        cursor: pointer;
      }
    }

    .el-menu {
      height: 100%;
      height: calc(100% - 80px);
      border-radius: 0px;
      background-color: black;
      border-right: 0px;
      width: 200px;
    }

    .el-menu--collapse {
      width: 60px;
      .help_button{
        width: 60px;
      }
    }

    .el-menu-item, .el-submenu__title {
      color: white;
      text-align: left;
      height: 46px;
      line-height: 46px;
    }

    .el-menu-item:hover, .el-submenu .el-menu-item:hover, .el-submenu__title:hover {
      background-color: #3a8ee6;
    }

    .el-submenu .el-menu-item {
      background-color: black;
      min-width: 60px;

      &:hover {
        background-color: #3a8ee6;
      }
    }
    .help_button{
      color: white;
      background-color: transparent;
      border: 0;
      width: 100%;
      height: 50px;
      &:hover{
        color: #3a8ee6;
      }
    }
  }
</style>
