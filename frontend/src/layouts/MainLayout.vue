<template>
  <div class="wrapper">
    <div class="item-header" ref="header">
      <Navbar/>
    </div>
    <div class="item-body" v-bind:style="styleContent">
      <router-view/>
    </div>
    <div class="item-footer" ref="footer">
      <Footer/>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default {
  name: "MainLayout",
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
      styleContent: {
        'min-height': ''
      }
    }
  },
  methods: {
    heightContent() {
      let heightNavbar = this.$refs.header.clientHeight;
      let heightFooter = this.$refs.footer.clientHeight;
      let layoutBlock = heightNavbar + heightFooter;
      let totalHeight = document.documentElement.clientHeight;
      if (totalHeight === 568) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 39) + 'px';
      } else if(totalHeight === 640) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 47) + 'px';
      } else if (totalHeight === 653) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 40) + 'px';
      } else if (totalHeight === 667) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 51) + 'px';
      } else if (totalHeight === 731) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 60) + 'px';
      } else if (totalHeight === 736) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 61) + 'px';
      } else if (totalHeight === 812) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 57) + 'px';
      } else if (totalHeight === 823) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 65) + 'px';
      } else if (totalHeight === 1024) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 130) + 'px';
      } else if (totalHeight === 1366) {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 123) + 'px';
      } else {
        this.styleContent["min-height"] = (totalHeight - layoutBlock - 39) + 'px';
      }
    }
  },
  mounted() {
    this.heightContent();
  }
}
</script>

<style scoped>
.wrapper {
  /*min-height: 100%;*/
  /*display: flex;*/
  /*flex-direction: column;*/
}

.item-header,
.item-footer {
  /*flex-shrink: 0;*/
}

.item-body {
  /*flex-grow: 1;*/
}

/*media queries**************************************************************/
/*@media screen and (max-width: 1024px) {*/
/*  .item-body {*/
/*    min-height: 1080px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 768px) {*/
/*  .item-body {*/
/*    min-height: 714px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 450px) {*/
/*  .item-body {*/
/*    min-height: 323px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 414px) {*/
/*  .item-body {*/
/*    min-height: 480px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 411px) {*/
/*  .item-body {*/
/*    min-height: 476px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 375px) {*/
/*  .item-body {*/
/*    min-height: 560px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 360px) {*/
/*  .item-body {*/
/*    min-height: 398px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 320px) {*/
/*  .item-body {*/
/*    min-height: 334px;*/
/*  }*/
/*}*/

/*@media screen and (max-width: 280px) {*/
/*  .item-body {*/
/*    min-height: 418px;*/
/*  }*/
/*}*/
</style>