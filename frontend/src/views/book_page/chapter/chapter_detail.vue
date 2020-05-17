<template>
  <div class="chapter_container">
    <header class="chapter_header">
      <div class="header_top">
        <div class="breadcrumb_set">
          <el-breadcrumb separator="/" v-bind="chapter">
            <el-breadcrumb-item><span>Main</span></el-breadcrumb-item>
            <el-breadcrumb-item><span>{{chapter.type}}</span></el-breadcrumb-item>
            <el-breadcrumb-item><span>{{chapter.name}}</span></el-breadcrumb-item>
            <el-breadcrumb-item><span>Chapter</span></el-breadcrumb-item>
          </el-breadcrumb>
        </div>
        <div class="text_setting">
          <el-select v-model="choices.font_size" style="width: 100px" placeholder="Size">
            <el-option label="16pt" value="16"/>
            <el-option label="18pt" value="18"/>
            <el-option label="20pt" value="20"/>
            <el-option label="22pt" value="22"/>
            <el-option label="24pt" value="24"/>
          </el-select><!--font-->
          <el-select v-model="choices.background" style="width: 100px" placeholder="Background">
            <el-option style="background-color: lightyellow" label="lightyellow" value="lightyellow"/>
            <el-option style="background-color: lightsteelblue" label="lightsteelblue" value="lightsteelblue"/>
            <el-option style="background-color: lightskyblue" label="lightskyblue" value="lightskyblue"/>
          </el-select><!--background color-->
          <el-select v-model="choices.font_family" style="width: 100px" placeholder="Font">
            <el-option label="Arial" value="Arial ,sans-serif"/>
            <el-option label="Roboto" value="Roboto ,sans-serif"/>
            <el-option label="Courier" value="Courier ,sans-serif"/>
          </el-select><!--font-family-->
          <el-select v-model="choices.text_color" style="width: 150px" placeholder="Text color">
              <el-option label="Default" value="#000"/>
              <el-option label="Purple" value="#9370DB"/>
              <el-option label="Green" value="#2E8B57"/>
              <el-option label="DarkSlateGray" value="#2F4F4F"/>
              <el-option label="Steel blue" value="#778899"/>
              <el-option label="Maroon" value="#800000"/>
              <el-option label="Cyan" value="#6A5ACD"/>
              <el-option label="Rosy brown" value="#BC8F8F"/>
              <el-option label="Brown" value="#F4A460"/>
              <el-option label="Beige" value="#F5F5DC"/>
              <el-option label="White" value="#F5F5F5"/>
          </el-select><!---->
        </div>
      </div>
      <div class="chapter_info">
        <h2 class="chapter_name">Chapter Name</h2>
        <div class="button_group">
          <el-button-group>
            <el-button>Previous</el-button>
            <el-button><router-link :to="{name:'book'}">Index</router-link></el-button>
            <el-button>Next</el-button>
            <el-button>Book Mark</el-button>
          </el-button-group>
        </div>
      </div>
    </header>
    <el-main>

      <p v-bind:style="changeStyle()" class="default_text">
        Lorem ipsum dolor sit amet, pro te suscipit consectetuer. Integre postulant te eum, te iriure option dissentias
        sit. Ne pri magna malis expetendis, duo ei viris decore nusquam. Te sumo conclusionemque qui, in sea aliquid
        delicata. Ad cum clita democritum concludaturque, sed ei dicat causae. Sanctus abhorreant te vix.
        <br/>
        Iriure integre oblique no est. Unum vituperatoribus nam te, saepe tempor gubergren ei his, an essent accusam
        mnesarchum pro. Quo ut etiam zril phaedrum, ad modus alienum nam, fuisset tibique pro et. Est singulis
        sententiae id, ei per simul iisque civibus. Etiam virtute accusamus ei sed, tempor patrioque aliquando cu duo.
        <br/>
        Et quem omnis eleifend has. Et regione albucius cum, nam meis soleat eu. Mea facilis detracto an, impetus
        aeterno ei vim, in albucius vituperatoribus vis. Iudico aperiri oporteat no eos. In pri alia partiendo, ea pro
        ferri facer efficiantur, ei eos ferri labitur molestiae.
        <br/>
        Choro ridens volutpat et vix, quem antiopam ocurreret eu pri. An similique consetetur est, vidit audiam
        tincidunt nec te, probo periculis consequuntur eu pri. Vim elitr ocurreret cu, vel te paulo pericula. Vix homero
        possit id, ea usu nominati repudiare.
        <br/>
        Ea graeci eloquentiam sea, ad habeo eleifend cum. Wisi ubique assueverit vel an. Usu veri percipit ex. Te sea
        diam cibo noluisse. Amet sumo ex vis. Nec id utamur quaestio, ex eum graeco debitis signiferumque, ius fastidii
        propriae argumentum at.
        <br/>
        Mei cibo fabulas aliquando te, et corpora tractatos honestatis ius, vix putant habemus deseruisse no. Te admodum
        rationibus vel. Et vim dicant noluisse corrumpit. Ex laoreet impedit postulant pro.
        <br/>
        Usu ad viris ancillae propriae, fugit commodo gubergren mea ex. Quo dictas nominavi patrioque eu, augue nominavi
        singulis in duo. Quod diam pro an, pri ad vero euismod omnesque. Est ad meis graeco omittantur, mei quem
        menandri ne. Eos in eleifend dignissim, consul integre pri ut, natum indoctum vis id. Id putant dolorem accusata
        per, vix at velit volutpat.
        <br/>
        Vel ludus exerci dolorem et. Quot praesent mel in. His causae mollis an. Eos an splendide disputationi. Est no
        aliquam pertinax indoctum.
        <br/>
        Modus nominavi assentior id vis, ea vis paulo putent virtute, per ea ludus temporibus disputando. In cum blandit
        interesset, tempor facete inermis id cum. In mel vocibus urbanitas. Ne doming eligendi euripidis nec. Laoreet
        repudiandae vel cu, eu zril sententiae vel.
        <br/>
        Tantas munere doming pri ne, ut eirmod scriptorem est. Ad has hinc atqui mentitum. Eum eu consul semper,
        facilisis definitionem an eam. Legimus singulis cu qui, per in homero reprehendunt, te copiosae elaboraret eum.
        Quo affert numquam ei, vivendum maluisset dignissim eum in, ea odio repudiare vituperatoribus vim. Ius purto
        graece alterum ex.
      </p>
    </el-main>
    <div class="chapter_info">
      <div class="button_group">
        <el-button-group>
          <el-button>Previous</el-button>
          <el-button><router-link :to="{name:'book'}">Index</router-link></el-button>
          <el-button>Next</el-button>
          <el-button>Book Mark</el-button>
        </el-button-group>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: "chapter_detail",
    data() {
      return {
        chapter: {

        },
        choices:{
          font_size:'',
          background:'',
          font_family:'',
          text_color:''
        }
      }
    },
    props:{
      url: String
    },
    created() {
      this.getChapter()
    },
    methods:{
      getChapter(){
        axios.get(this.$props.url).then((response)=>{
          console.log(response.data)
        })
      },
      changeStyle(){

      }
    }
  }
</script>

<style lang="less" scoped>

  .chapter_container {
    .chapter_header {
      height: 100%;
      padding: 0 20px;
      display: block;

      .header_top {
        height: 30px;
        margin-bottom: 20px;

        .breadcrumb_set {
          display: block;
          float: left;

          .el-breadcrumb__item span {
            font-size: 20px;
            line-height: 30px;
          }
        }

        .text_setting {
          float: right;
        }
      }
    }

    .chapter_info {
      .chapter_name {
        text-align: center;
        margin-bottom: 10px;
      }

      .button_group {
        margin: 0 auto;
        width: 400px;

        .el-button {
          width: 100px;
        }
      }
    }

    .default_text{
      font-size: 20px;
      font-family: Calibri Light,sans-serif;
      background-color: white;
      color: black;
    }
  }
</style>
<style>

</style>
