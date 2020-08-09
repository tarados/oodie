<template>
  <div class="wrapper" @visible="visible">
    <div class="item-header" ref="header" >
      <Navbar
          ref="navbar"
      />
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
                },
                visibleCard: false
            }
        },
        methods: {
            visible(val) {
                this.$refs.navbar.visibleCard = false;
                console.log(this.$refs.navbar.visibleCard);
                console.log(val);
            },
            heightContent() {
                let heightNavbar = this.$refs.header.clientHeight;
                let heightFooter = this.$refs.footer.clientHeight;
                let layoutBlock = heightNavbar + heightFooter;
                console.log(layoutBlock);
                let totalHeight = document.documentElement.clientHeight;
                console.log(totalHeight);
                if (totalHeight === 568) {
                    this.styleContent["min-height"] = (totalHeight - layoutBlock - 39) + 'px';
                } else if (totalHeight === 640) {
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
            this.visible();
            this.heightContent();
        }
    }
</script>

<style scoped>

</style>