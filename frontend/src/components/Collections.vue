<template>
  <div class="wrapper_collections">
    <div class="collections">
      <div v-for="item in items" :key="item.linkImage" class="item_collections">
        <img :src="item.linkImage">
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
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/corgi_8e1c1d7e-58b2-4b1d-886c-bfd9fdfc33cf_600x600.jpg?v=1587716048',
                        price: '$396.00'
                    },
                    {
                        title: 'Oodie Twin Pack',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/CORGI_1e12bd25-a8db-4256-8f03-c3c48dfcd35d_600x600.jpg?v=1587724887',
                        price: '$239.00'
                    },
                    {
                        title: 'Nap Bundle (SOLD OUT)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/corgi_b364b30f-ecba-4f25-82c3-87f0be0c00ac_600x600.jpg?v=1587715600',
                        price: '$198.00'
                    },
                    {
                        title: 'German Shepherd Oodie (Sent 12th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-163_1024x1024_2x_d8e6934a-b0c7-4495-a622-f4cfbab78136_600x600.jpg?v=1587714781',
                        price: '$138.00'
                    },
                    {
                        title: 'Navy Oodie (Sent 25th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-229_1024x1024_2x_2e262993-c336-4851-861b-64783759e942_600x600.jpg?v=1587715848',
                        price: '$448.00'
                    },
                    {
                        title: 'Pink Oodie (Sent 25th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-104_1024x1024_2x_e5fdf768-1bf0-4d64-8b49-ad57806cb994_600x600.jpg?v=1587725875',
                        price: '$218.00'
                    },
                    {
                        title: 'Grey Oodie (Sent 25th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-3_1024x1024_2x_14d910a4-585b-4268-86e6-4e25f1ecb07a_600x600.jpg?v=1587714844',
                        price: '$99.00'
                    },
                    {
                        title: 'Pizza Oodie (Sent 12th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-256_1024x1024_2x_689c87dd-49ea-4fac-80a8-2110550b3287_600x600.jpg?v=1587726046',
                        price: '$99.00'
                    },
                    {
                        title: 'Panda Oodie (Sent 17th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/imgpsh_fullsize_anim1_600x600.jpg?v=1587725727',
                        price: '$99.00'
                    },
                    {
                        title: 'Cat Oodie (Sent 12th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-147_1024x1024_2x_7d7e551e-2634-4220-8635-453796a2ef87_600x600.jpg?v=1587714379',
                        price: '$99.00'
                    },
                    {
                        title: 'Otter Oodie (Sent 15th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OtterOodieImage1_600x600.jpg?v=1589560549',
                        price: '$99.00'
                    },
                    {
                        title: 'Sloth Oodie (Sent 17th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-117_1024x1024_2x_68cb176b-4db8-4849-9287-483d87e4ca2b_600x600.jpg?v=1587726718',
                        price: '$99.00'
                    },
                    {
                        title: 'Unicorn Oodie (Sent 17th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-213_1024x1024_2x_e0584fbb-e649-46e6-a7ff-ddf2a5acbf1c_600x600.jpg?v=1587727115',
                        price: '$99.00'
                    },
                    {
                        title: 'Bulldog Oodie (Sent 17th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/BullDogOodieImage1_600x600.jpg?v=1589560671',
                        price: '$99.00'
                    },
                    {
                        title: 'Garlic Bread Oodie (Sent 12th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-245_1024x1024_2x_f22a30ef-4193-4454-a4ba-48a295bae9eb_600x600.jpg?v=1587714710',
                        price: '$99.00'
                    },
                    {
                        title: 'Bunny Oodie (Sent 12th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/BunnyOodieImage1_600x600.jpg?v=1589560670',
                        price: '$99.00'
                    },
                    {
                        title: 'Avocado Oodie (Sent 4th August)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/AvocadoOodieImage2_600x600.jpg?v=1589560548',
                        price: '$99.00'
                    },
                    {
                        title: 'Koala Oodie (Sent 25th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-240_1024x1024_2x_6153d70d-59d6-4b24-b3b6-62e749603391_600x600.jpg?v=1587715279',
                        price: '$99.00'
                    },
                    {
                        title: 'Corgi Oodie (Sent 17th July)',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/OODIE_FINALS_-128_1024x1024_2x_561f703b-a2ca-4089-884f-05a40c488627_600x600.jpg?v=1587714645',
                        price: '$99.00'
                    },
                    {
                        title: 'The Oodie Trackies',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/comfy_trackies-2_600x600.jpg?v=1587726987',
                        price: '$99.00'
                    },
                    {
                        title: 'Grey Oodie Boots',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/Australian_Slippers_and_Boots-15_600x600.jpg?v=1587715060',
                        price: '$99.00'
                    },
                    {
                        title: 'Oodie Slippers',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/Australian_Slippers_and_Boots-8_600x600.jpg?v=1587716266',
                        price: '$99.00'
                    },
                    {
                        title: 'Navy Oodie Boots',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/Australian_Slippers_and_Boots-18_1080x_b3099646-968d-4507-bde7-8f5b12b13cce_600x600.jpg?v=1587715967',
                        price: '$59.99'
                    },
                    {
                        title: 'Pink Oodie Boots',
                        linkImage: 'https://cdn.shopify.com/s/files/1/0023/7427/1029/products/Australian_Slippers_and_Boots-2_600x600.jpg?v=1587725977',
                        price: '$40.00'
                    },

                ]
            }
        }
    }
</script>

<style scoped>

</style>