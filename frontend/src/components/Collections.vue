<template>
  <div class="wrapper">
    <div class="header">
      <h2>which will you choose?</h2>
    </div>
    <div class="row">
      <div v-for="item in items" :key="item.linkImage" class="item">
        <img :src="item.linkImage">
        <h4>{{item.title}}</h4>
        <p>{{item.price}}</p>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Collections",
        data() {
            return {
                items: [
                    {
                        title: 'Oodie Family Pack',
                        linkImage: '/img/Oodie_Family_Pack.jpg',
                        price: '$396.00'
                    },
                    {
                        title: 'Oodie Twin Pack',
                        linkImage: '/img/Oodie_Twin_Pack.jpg',
                        price: '$239.00'
                    },
                    {
                        title: 'Nap Bundle (SOLD OUT)',
                        linkImage: '/img/Nap_Bundle_(SOLD_OUT).jpg',
                        price: '$198.00'
                    },
                    {
                        title: 'German Shepherd Oodie (Sent 12th July)',
                        linkImage: '/img/German_Shepherd_Oodie_(Sent_12th_July).jpg',
                        price: '$138.00'
                    },
                    {
                        title: 'Navy Oodie (Sent 25th July)',
                        linkImage: '/img/Navy_Oodie_(Sent_25th_July).jpg',
                        price: '$448.00'
                    },
                    {
                        title: 'Pink Oodie (Sent 25th July)',
                        linkImage: '/img/Pink_Oodie_(Sent_25th_July).jpg',
                        price: '$218.00'
                    },
                    {
                        title: 'Grey Oodie (Sent 25th July)',
                        linkImage: '/img/Grey_Oodie_(Sent_25th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Pizza Oodie (Sent 12th July)',
                        linkImage: '/img/Pizza_Oodie_(Sent_12th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Panda Oodie (Sent 17th July)',
                        linkImage: '/img/Panda_Oodie_(Sent_17th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Cat Oodie (Sent 12th July)',
                        linkImage: '/img/Cat_Oodie_(Sent_12th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Otter Oodie (Sent 15th July)',
                        linkImage: '/img/Otter_Oodie_(Sent_15th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Sloth Oodie (Sent 17th July)',
                        linkImage: '/img/Sloth_Oodie_(Sent_17th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Unicorn Oodie (Sent 17th July)',
                        linkImage: '/img/Unicorn_Oodie_(Sent_17th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Bulldog Oodie (Sent 17th July)',
                        linkImage: '/img/Bulldog_Oodie_(Sent_17th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Garlic Bread Oodie (Sent 12th July)',
                        linkImage: '/img/Garlic_Bread_Oodie_(Sent_12th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Bunny Oodie (Sent 12th July)',
                        linkImage: '/img/Bunny_Oodie_(Sent_12th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Avocado Oodie (Sent 4th August)',
                        linkImage: '/img/Avocado_Oodie_(Sent_4th_August).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Koala Oodie (Sent 25th July)',
                        linkImage: '/img/Koala_Oodie_(Sent_25th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Corgi Oodie (Sent 17th July)',
                        linkImage: '/img/Corgi_Oodie_(Sent_17th_July).jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'The Oodie Trackies',
                        linkImage: '/img/The_Oodie_Trackies.jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Grey Oodie Boots',
                        linkImage: '/img/Grey_Oodie_Boots.jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Oodie Slippers',
                        linkImage: '/img/Oodie_Slippers.jpg',
                        price: '$99.00'
                    },
                    {
                        title: 'Navy Oodie Boots',
                        linkImage: '/img/Navy_Oodie_Boots.jpg',
                        price: '$59.99'
                    },
                    {
                        title: 'Pink Oodie Boots',
                        linkImage: '/img/Pink_Oodie_Boots.jpg',
                        price: '$40.00'
                    },

                ]
            }
        }
    }
</script>

<style scoped>
  .wrapper {
    border: 1px solid red;
    margin-top: 55px;
  }

  .header {
    margin-bottom: 55px;
  }

  .header h2 {
    text-transform: uppercase;
    letter-spacing: 0.1em;
    /*font-family: "montreal-serialbold";*/
    font-weight: 600;
    font-size: 23px;
  }

  .row {
    max-width: 1200px;
    margin: 0 auto;
    border: 1px solid black;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    align-content: center;
  }

  .item {
    margin: 0 auto;
    padding-bottom: 20px;
    border: 1px solid green;
    width: 48%;
    min-width: 37vmax;
  }

  .item img {
    width: 100%;
  }



</style>